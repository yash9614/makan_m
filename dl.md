
# Assignment: Visual Sort with Transfer Learning (PyTorch)

**Repo to put this in:** [yash9614/lear_deepintodl](https://github.com/yash9614/lear_deepintodl)  
**Style reference:** [suneelbvs/Deep-Learning-Projects](https://github.com/suneelbvs/Deep-Learning-Projects) (CNN + MobileNet / VGG bake-off, not tensor drills)  
**Assumes you already did:** Codebasics notebooks 1–3, plus your `PyTorch_Exercise` / `NeuralNetworks_*` work.  
**Do not do:** `torch.tensor` tutorials, from-scratch autograd, MNIST “hello world.”

Time box: **one focused session (about 2–3 hours)**, not a weekend project.  
Hardware: Colab GPU is enough. CPU works if you keep the subset small.

Suggested folder:

```text
lear_deepintodl/
  Industry_TransferLearning_VisualSort/
    ASSIGNMENT.md          ← this file
    visual_sort.ipynb      ← your work
    notes.md               ← answers to the concept questions
```

---

## 0. Why this assignment exists

Industry computer-vision work almost never trains a CNN from random weights on 50k images when a pretrained backbone already exists.

The job looks like this:

1. You get a **small labeled set** for *your* classes.
2. You start from **ImageNet weights**.
3. You **freeze** most of the network, train a new head.
4. You maybe **unfreeze** the last block and fine-tune gently.
5. You report **more than accuracy**, because a 90% model can still be useless on the rare class.
6. You **save the weights** and run one inference like a teammate would.

That is the same idea as the MobileNet vs VGG notebooks in Suneel’s repo. You will do a smaller, cleaner version and explain *why* each step exists.

Business story (keep it; it is not decoration):

> A warehouse camera should sort incoming packages into three visual buckets: **vehicle-like / animal-like / other-object**. You only have a few thousand labeled stills. Training ResNet from scratch is the wrong default. Transfer learning is the default.

You will simulate that with a **3-class subset of CIFAR-10**:

| Class id | CIFAR-10 label | Your bucket |
|---:|---|---|
| 1 | automobile | vehicle |
| 3 | cat | animal |
| 8 | ship | other-object |

Three classes, real pixels, short training. Not FashionMNIST again.

---

## 1. Concepts to lock before you write a training loop

Write these in `notes.md` in your own words. If you cannot explain one of them, do not start coding that part yet.

### 1.1 What a pretrained CNN actually stores

A ResNet/MobileNet trained on ImageNet has already learned **generic visual features**: edges, textures, object parts.

- Early layers: local patterns (edges, color blobs).
- Later layers: more class-specific parts.

Transfer learning means: **reuse the feature extractor, replace the classifier head.**

Question A: If ImageNet has no “ship” class, why can those weights still help you classify ships?

### 1.2 Backbone vs head

```text
image
  → backbone (conv blocks, already trained)
  → pooling
  → head (new Linear layer(s) for YOUR 3 classes)
```

Two training modes you must implement and compare:

| Mode | Backbone | Head | Learning rate |
|---|---|---|---|
| Feature extraction | `requires_grad = False` | train | larger, e.g. 1e-3 |
| Fine-tune last block | unfreeze last stage only | train | smaller, e.g. 1e-4 |

Question B: What goes wrong if you unfreeze the whole ResNet and use `lr=1e-3` on 3k images?

### 1.3 Why CIFAR images need a transform

CIFAR is 32×32. ImageNet backbones expect ~224×224 and ImageNet mean/std.

So you **resize + normalize with the backbone’s stats**, not “whatever looks nice.”

Question C: What happens if you feed 32×32 tensors straight into `resnet18` with no resize/normalize?

### 1.4 Metrics that matter

Accuracy on a balanced 3-class set can hide a model that never predicts “animal.”

You will compute:

- accuracy
- per-class precision, recall, F1
- confusion matrix

Question D: In the warehouse story, which error is worse — calling a cat a ship, or calling a car an animal? There is no single right answer; pick one and justify it. That is how product metrics get chosen.

### 1.5 Overfitting signature

Plot train loss vs val loss.

| Curve | Meaning |
|---|---|
| both falling | still learning |
| train falling, val rising | memorizing |
| both flat high | LR too small, frozen too hard, or data bug |

Question E: If val accuracy is 92% but val loss is rising, do you ship the last epoch or an earlier checkpoint? Why?

---

## 2. Constraints (do not ignore these)

- Framework: **PyTorch** (+ `torchvision`).
- Model: start with **`resnet18`** from `torchvision.models` with ImageNet weights. Optional second backbone: `mobilenet_v2` (this is the Suneel-style bake-off).
- Data: CIFAR-10, **only classes {1, 3, 8}**.
- Cap: **≤ 8 epochs** per run. If it needs 30 epochs, your setup is wrong.
- Batch size: 64 if GPU, 32 if CPU.
- You must use `Dataset` / `DataLoader`. No manual mini-batch indexing.
- You must save `best.pt` from **validation** score, not training accuracy.
- No copy-paste of your existing `CNN_Exercise` or `Transfer_Learning_Solutions.ipynb` as the submission. You may read them. You may not submit them.

---

## 3. Tasks

### Task 0 — Inspect, don’t train (15 min)

1. Load CIFAR-10.
2. Keep only the three classes. Print counts per class for train and test.
3. Show 8 example images with labels.
4. Write one sentence: is this balanced enough to trust raw accuracy?

### Task 1 — Data pipeline (20 min)

Build:

- train split from the official train set (e.g. 80%)
- val split from the official train set (e.g. 20%)
- test = official test set, filtered to 3 classes

Transforms:

- train: Resize(224), RandomHorizontalFlip, ToTensor, ImageNet Normalize
- val/test: Resize(224), ToTensor, ImageNet Normalize

ImageNet mean/std:

```text
mean = [0.485, 0.456, 0.406]
std  = [0.229, 0.224, 0.225]
```

Checkpoint: one train batch should be shape `[B, 3, 224, 224]`.

### Task 2 — Model factory (20 min)

Write `make_model(num_classes=3, freeze_backbone=True)`:

- load `resnet18` with pretrained weights
- replace `model.fc` with `nn.Linear(model.fc.in_features, 3)`
- if `freeze_backbone`: set `requires_grad=False` on all parameters except the new `fc`

Print the number of **trainable** parameters in both modes.

Question F: Why is the frozen model so much cheaper to train?

### Task 3 — Train feature extractor (30–40 min)

- freeze backbone
- `CrossEntropyLoss`
- `Adam` on trainable params only
- 5–8 epochs
- each epoch: train loss/acc, val loss/acc
- save weights when **val loss** is best

Do not tune 12 hyperparameters. One honest run.

### Task 4 — Evaluate like an adult (20 min)

On the **test** set, using `best.pt`:

- overall accuracy
- classification report (per-class P/R/F1)
- confusion matrix plot

Then write 5–8 lines:

- which class is weakest
- whether errors make visual sense (cat vs ship vs car)
- whether you would deploy this at 224px warehouse-cam quality

### Task 5 — Fine-tune last block (30 min, optional but recommended)

Starting from the frozen best checkpoint:

1. Unfreeze `layer4` (ResNet18’s last stage) + `fc`.
2. Use a **smaller** LR.
3. Train 3–5 more epochs.
4. Compare test F1 / accuracy to Task 3.

Question G: Did fine-tuning help, hurt, or do nothing? Tie the answer to the loss curves, not to vibes.

### Task 6 — Inference demo (10 min)

Load `best.pt`, pick **one** test image, print:

- predicted class
- probability / logits
- true class

This is the “show a teammate” cell.

### Task 7 — Optional bake-off

Repeat Task 3 with `mobilenet_v2` instead of ResNet18 (replace its classifier).  
One table:

```text
backbone     trainable params    test acc    macro F1    minutes
resnet18     ...
mobilenet_v2 ...
```

This is the industry move from Suneel’s “vgg16 vs mobilenetv2 who wins” notebooks, at assignment scale.

---

## 4. Training loop you should be able to explain

You already wrote a loop in the Codebasics / `NeuralNetworks_Training_Exercise` work. Here the only new discipline is **eval mode + no grad on val/test**.

Every epoch:

```text
model.train()
for xb, yb in train_loader:
    opt.zero_grad()
    logits = model(xb)
    loss = criterion(logits, yb)
    loss.backward()
    opt.step()

model.eval()
with torch.no_grad():
    for xb, yb in val_loader:
        ... accumulate val loss/acc

if val_loss < best:
    save state_dict
```

Question H: Why `model.eval()` on validation even though dropout may be off in ResNet’s default head? (Hint: BatchNorm.)

---

## 5. Deliverables

1. `visual_sort.ipynb` — runs top to bottom on Colab.
2. `notes.md` — answers A–H, plus the Task 4 write-up.
3. `best.pt` — optional to commit (often too large). At least show the save cell ran.
4. One screenshot or printed confusion matrix in the notebook.

Not required: Streamlit app, Docker, TinyML, custom CUDA.

---

## 6. Self-score (honest)

Give yourself 0 / 1 / 2 on each:

- [ ] 3-class subset is correct; counts printed
- [ ] DataLoader batch is `B×3×224×224`
- [ ] Frozen vs trainable param counts printed
- [ ] Val used to pick checkpoint
- [ ] Test report + confusion matrix
- [ ] Notes A–H are actual explanations, not one-liners
- [ ] Fine-tune comparison or a written reason you skipped it
- [ ] Single-image inference cell

12+ is a pass. Below 10 means you trained something but did not finish the *assignment*.

---

## 7. How this sits on your existing repo

| You already touched | This assignment adds |
|---|---|
| Tensors, `nn.Module`, basic fit loop | Pretrained backbone as a default |
| FashionMNIST CNN exercise | Real transfer protocol + ImageNet norm |
| Flowers transfer notebook | Explicit freeze vs last-block fine-tune |
| Churn regularization | CV metrics + confusion matrix on images |
| Hyperparameter exercise | *Not* a search. One constrained comparison |
| Suneel MobileNet/VGG projects | Same question, smaller data, written reasoning |

Next assignment after this (do not start it now): take your `spam.csv` / BERT notebook and apply the **same protocol** — freeze encoder, train head, then unfreeze last layers, report F1 not accuracy. Same skeleton, different modality.

---

## 8. Hints without giving the notebook away

```python
from torchvision.models import resnet18, ResNet18_Weights
weights = ResNet18_Weights.DEFAULT
model = resnet18(weights=weights)
```

Filter CIFAR targets with a map `{1:0, 3:1, 8:2}` so loss sees `0..2`.

`torchvision.datasets.CIFAR10` can stay; wrap or filter indices. Do not download a new 10GB dataset.

If Colab RAM complains, drop `num_workers` to 0 and keep 224 resize. Do not go back to 32×32 just to make it “faster” — that breaks the pretrained contract.

---

## 9. Definition of done

You can explain, out loud, without the notebook:

1. What you reused from ImageNet and what you trained.
2. Why val loss picked the file you would send to a teammate.
3. Which class the model confuses, and whether fine-tuning changed that.

If you can only say “accuracy went up,” the assignment is not done.
