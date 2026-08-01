# TensorTonic Solutions

Welcome to my TensorTonic solutions repository!

Here you'll find my solutions to various machine learning and deep learning problems from [TensorTonic](https://tensortonic.com).

## What is TensorTonic?

TensorTonic is a platform where you can implement core algorithms of Machine Learning from scratch.

This repository contains my personal solutions to these problems, automatically synchronized from the platform.

<!-- tensortonic:start -->
# Henry Ngo's TensorTonic Solutions

Verified machine learning implementations completed on [TensorTonic](https://www.tensortonic.com).

<p align="center">
  <img src="https://www.tensortonic.com/api/badge/huyngo.svg" alt="TensorTonic Verified Solutions" width="100%" />
</p>

| Problem | Description | Link |
|---|---|---|
| AdaGrad Optimizer | Implement a vectorized AdaGrad update in NumPy with accumulated squared gradients and adaptive per-parameter learning rates. | https://www.tensortonic.com/problems/adagrad-optimizer |
| Implement Adam Optimizer Step | Implement one vectorized Adam optimizer step in NumPy with first and second moments, bias correction, and elementwise parameter updates. | https://www.tensortonic.com/problems/adam-optimizer |
| Implement AdamW (Decoupled Weight Decay) | Implement one AdamW optimizer step in NumPy with first and second moments plus decoupled weight decay. | https://www.tensortonic.com/problems/adamw-optimizer |
| Angle Between 3D Vectors | Compute the angle between two 3D vectors in NumPy with clamped cosine values and safe handling of zero norms. | https://www.tensortonic.com/problems/angle-between-3d |
| Bag-of-Words Vector | Build a NumPy bag-of-words count vector from an ordered vocabulary while ignoring out-of-vocabulary tokens. | https://www.tensortonic.com/problems/bag-of-words |
| Bernoulli Probability Mass Function & Moments | Compute the Bernoulli probability mass function, expected value, and variance for a valid success probability. | https://www.tensortonic.com/problems/bernoulli-pmf |
| Binning | Assign numeric values to ordered bins using supplied boundaries while handling values at interval edges. | https://www.tensortonic.com/problems/binning |
| Color to Grayscale | Convert an RGB image to grayscale using weighted color channels while preserving its spatial dimensions. | https://www.tensortonic.com/problems/color-to-grayscale |
| Cosine Annealing LR Scheduler | Compute a cosine-annealed learning rate between configured maximum and minimum values across training steps. | https://www.tensortonic.com/problems/cosine-annealing-lr |
| Cosine Embedding Loss | Compute cosine embedding loss for similar and dissimilar vector pairs using labels and a configurable margin. | https://www.tensortonic.com/problems/cosine-embedding-loss |
| Implement Cosine Similarity | Compute cosine similarity between NumPy vectors with dot products, Euclidean norms, and zero-vector handling. | https://www.tensortonic.com/problems/cosine-similarity |
| Cyclic Encoding | Encode periodic numeric features as sine and cosine coordinates using a specified cycle length. | https://www.tensortonic.com/problems/cyclic-encoding |
| Data Drift Detection | Detect feature drift by computing total variation distance between reference and production histograms. | https://www.tensortonic.com/problems/data-drift-detection |
| Implement Dice Loss | Compute Dice loss for segmentation predictions using overlap, total mass, and a numerical smoothing term. | https://www.tensortonic.com/problems/dice-loss |
| Differencing | Transform a time series into lagged differences while preserving the requested differencing interval. | https://www.tensortonic.com/problems/differencing |
| Implement Dot Product | Implement the dot product of equal-length numeric vectors by summing element-wise products without library shortcuts. | https://www.tensortonic.com/problems/dot-product |
| Implement Dropout (Training Mode) | Implement training-mode dropout in NumPy with random masking and inverted scaling of retained activations. | https://www.tensortonic.com/problems/dropout-training |
| Edit Distance | Compute Levenshtein edit distance between two strings using dynamic programming over insertions, deletions, and substitutions. | https://www.tensortonic.com/problems/edit-distance |
| Calculate Eigenvalues of a Matrix | Calculate the eigenvalues of a square matrix and return them in the format required by the numerical contract. | https://www.tensortonic.com/problems/eigenvalues |
| ELU Activation | Apply the ELU activation element-wise, retaining positive inputs and exponentially transforming negative values. | https://www.tensortonic.com/problems/elu-activation |
| ε-Greedy Action Selection | Select a reinforcement-learning action with epsilon-greedy exploration using action values and controlled randomness. | https://www.tensortonic.com/problems/epsilon-greedy |
| Implement Euclidean Distance | Compute Euclidean distance between equal-length NumPy vectors as the square root of summed squared differences. | https://www.tensortonic.com/problems/euclidean-distance |
| Expected Value (Discrete Distribution) | Compute the expected value of a discrete distribution from matched outcomes and normalized probabilities. | https://www.tensortonic.com/problems/expected-value-discrete |
| Implement GELU Activation (Gaussian Error Linear Unit) | Implement the Gaussian Error Linear Unit activation element-wise using the required GELU approximation. | https://www.tensortonic.com/problems/gelu |
| Geometric Probability Mass Function & Mean | Compute the geometric distribution probability mass and mean from a valid success probability. | https://www.tensortonic.com/problems/geometric-pmf-mean |
| Implement Gradient Descent for a 1D Quadratic | Optimize a one-dimensional quadratic with iterative gradient descent and return the parameter trajectory. | https://www.tensortonic.com/problems/gradient-descent-quadratic |
| Build a Mini GRU Cell (Forward Pass) | Implement a GRU cell forward pass with reset, update, and candidate gates for one sequence timestep. | https://www.tensortonic.com/problems/gru-cell-forward |
| He Initialization | Scale raw weights into the He uniform range using a bound derived from the layer fan-in. | https://www.tensortonic.com/problems/he-initialization |
| Implement Hinge Loss (Binary SVM) | Compute binary SVM hinge loss from signed labels and prediction scores using the required margin. | https://www.tensortonic.com/problems/hinge-loss |
| Hit Rate at K | Calculate recommendation hit rate at K by checking whether each user's relevant items appear in top-ranked results. | https://www.tensortonic.com/problems/hit-rate-at-k |
| Implement Huber Loss | Compute Huber loss with quadratic errors near zero and linear penalties beyond a configurable threshold. | https://www.tensortonic.com/problems/huber-loss |
| Jaccard Similarity | Compute Jaccard similarity between two collections as intersection size divided by union size. | https://www.tensortonic.com/problems/jaccard-similarity |
| Label Smoothing Loss | Compute multiclass cross-entropy with label smoothing by distributing target mass across all classes. | https://www.tensortonic.com/problems/label-smoothing-loss |
| Implement Leaky ReLU (with α) | Apply Leaky ReLU element-wise with a configurable negative slope while retaining positive inputs. | https://www.tensortonic.com/problems/leaky-relu |
| Linear Layer Forward | Implement a dense linear layer forward pass by multiplying inputs by weights and adding a bias vector. | https://www.tensortonic.com/problems/linear-layer-forward |
| Learning Rate Scheduler (Linear Decay) | Compute a linearly decaying learning rate across training steps between configured start and end values. | https://www.tensortonic.com/problems/linear-lr-scheduler |
| Linear Regression Closed Form | Fit linear regression with the closed-form normal equation and return coefficients for the supplied design matrix. | https://www.tensortonic.com/problems/linear-regression-closed-form |
| Log Transform | Apply a numerically safe logarithmic transform to numeric features using the required offset or base. | https://www.tensortonic.com/problems/log-transform |
| Logistic Regression Training Loop | Train binary logistic regression in NumPy using sigmoid probabilities, gradient descent, and learned weight and bias parameters. | https://www.tensortonic.com/problems/logistic-regression-training |
| Implement Majority Class Classifier | Fit a majority-class baseline and predict the most frequent training label for every requested sample. | https://www.tensortonic.com/problems/majority-classifier |
| Make Diagonal Matrix | Construct a square diagonal matrix from a one-dimensional vector while setting every off-diagonal entry to zero. | https://www.tensortonic.com/problems/make-diagonal |
| Implement Manhattan Distance | Compute Manhattan distance between equal-length vectors by summing absolute coordinate differences. | https://www.tensortonic.com/problems/manhattan-distance |
| Matrix Inverse | Compute a square matrix inverse in NumPy while returning no result for invalid, non-square, or singular inputs. | https://www.tensortonic.com/problems/matrix-inverse |
| Matrix Trace | Compute the trace of a square matrix by summing its main diagonal entries without changing the input. | https://www.tensortonic.com/problems/matrix-trace |
| Matrix Transpose | Implement matrix transpose in NumPy without built-in transpose helpers, preserving rectangular shapes and the original input. | https://www.tensortonic.com/problems/matrix-transpose |
| Max Pooling 2D | Apply non-overlapping 2D max pooling to rectangular inputs while discarding incomplete edge windows. | https://www.tensortonic.com/problems/max-pooling-2d |
| Mean, Median, Mode | Calculate the mean, median, and deterministic mode of a numeric collection, including tied frequencies. | https://www.tensortonic.com/problems/mean-median-mode |
| Mean Squared Error (MSE) | Compute mean squared error between predictions and targets by averaging their squared element-wise differences. | https://www.tensortonic.com/problems/mean-squared-error |
| Implement Micro-F1 | Compute multiclass micro-F1 by aggregating true positives, false positives, and false negatives across labels. | https://www.tensortonic.com/problems/metrics-f1-micro |
| Min-Max Scaling | Scale numeric values to a requested range using observed minimum and maximum values with constant-input handling. | https://www.tensortonic.com/problems/min-max-scaling |
| Implement Min-Max Normalization | Normalize each NumPy feature to the zero-to-one range with explicit handling for constant columns. | https://www.tensortonic.com/problems/minmax-normalization |
| Moving Median | Compute a moving median over complete fixed-size sliding windows in an ordered numeric time series. | https://www.tensortonic.com/problems/moving-median |
| Implement Nadam (Nesterov + Adam) | Implement one Nadam optimizer step in NumPy by combining Adam moments with Nesterov momentum. | https://www.tensortonic.com/problems/nadam-optimizer |
| Implement Nesterov Momentum (NAG) | Implement a Nesterov accelerated-gradient update using lookahead momentum and the current gradient. | https://www.tensortonic.com/problems/nesterov-momentum |
| Normalize 3D Vectors | Normalize a 3D vector to unit length in NumPy while returning the required result for a zero vector. | https://www.tensortonic.com/problems/normalize-3d |
| Ordinal Encoding | Map ordered categorical values to integer ranks using a supplied category ordering and preserve input order. | https://www.tensortonic.com/problems/ordinal-encoding |
| Percent Change | Compute period-over-period percentage changes in a numeric time series with defined initial-value handling. | https://www.tensortonic.com/problems/percent-change |
| Perplexity Computation | Compute language-model perplexity from token probability distributions and the observed token indices. | https://www.tensortonic.com/problems/perplexity-computation |
| Popularity Ranking | Rank items by interaction popularity with deterministic ordering for equal-frequency items. | https://www.tensortonic.com/problems/popularity-ranking |
| Implement R² Score (Coefficient of Determination) | Compute the coefficient of determination from targets and predictions with explicit constant-target handling. | https://www.tensortonic.com/problems/r2-score |
| Random Forest Majority Vote | Combine multiple decision-tree predictions with majority voting and deterministic handling of tied classes. | https://www.tensortonic.com/problems/random-forest-vote |
| Implement ReLU Activation | Apply the ReLU activation element-wise by replacing negative values with zero and preserving nonnegative inputs. | https://www.tensortonic.com/problems/relu-activation |
| Remove Stopwords | Remove tokens found in a supplied stopword collection while preserving the order of remaining words. | https://www.tensortonic.com/problems/remove-stopwords |
| Ridge Regression | Fit ridge regression with L2 regularization using the closed-form solution required by the problem. | https://www.tensortonic.com/problems/ridge-regression |
| RMSProp Optimizer (Single Update Step) | Implement one RMSProp update in NumPy using an exponential squared-gradient average and adaptive scaling. | https://www.tensortonic.com/problems/rmsprop-optimizer |
| RNN Step Forward (Tanh Cell) | Implement one vanilla RNN timestep with affine input and recurrent transforms followed by tanh activation. | https://www.tensortonic.com/problems/rnn-step-forward |
| Sample Variance & Standard Deviation | Compute sample variance and standard deviation with Bessel's correction from a numeric collection. | https://www.tensortonic.com/problems/sample-var-std |
| Seasonal Average | Estimate seasonal averages by grouping time-series observations at the same position in each period. | https://www.tensortonic.com/problems/seasonal-average |
| SELU Activation | Apply SELU activation element-wise with scaled positive values and exponential negative values. | https://www.tensortonic.com/problems/selu-activation |
| Implement Sigmoid in NumPy | Implement a vectorized sigmoid activation in NumPy for scalars, lists, vectors, and matrices, including large positive and negative inputs. | https://www.tensortonic.com/problems/sigmoid-numpy |
| Implement Softmax Function | Implement numerically stable softmax by shifting logits before exponentiation and normalizing probabilities. | https://www.tensortonic.com/problems/softmax-function |
| Implement Swish Activation | Apply the Swish activation element-wise by multiplying each input by its sigmoid value. | https://www.tensortonic.com/problems/swish-activation |
| One-Sample t-Test | Compute a one-sample t-statistic in NumPy using the sample mean, Bessel-corrected deviation, and hypothesized mean. | https://www.tensortonic.com/problems/t-test-one-sample |
| Implement Tanh Activation | Implement the hyperbolic tangent activation element-wise with outputs bounded between minus one and one. | https://www.tensortonic.com/problems/tanh-activation |
| Text Chunking | Split text into ordered chunks under the requested size and overlap rules without dropping content. | https://www.tensortonic.com/problems/text-chunking |
| Top-K Recommendations | Return each user's highest-scoring unseen items with deterministic ranking and a configurable result limit. | https://www.tensortonic.com/problems/top-k-recommendations |
| Value Iteration Step | Perform one Bellman optimality update across states and actions for a tabular Markov decision process. | https://www.tensortonic.com/problems/value-iteration-step |
| Compute 3D Vector Norm | Compute the Euclidean norm of a 3D vector from the square root of summed squared coordinates. | https://www.tensortonic.com/problems/vector-norm-3d |
| Implement Wasserstein Critic Loss | Compute Wasserstein critic loss as the difference between mean fake and real critic scores. | https://www.tensortonic.com/problems/wasserstein-critic-loss |
| Word Count Dictionary | Count token occurrences in text and return a dictionary mapping each distinct word to its frequency. | https://www.tensortonic.com/problems/word-count-dict |
| Xavier Initialization | Scale raw weights into the Xavier uniform range using a bound derived from fan-in and fan-out. | https://www.tensortonic.com/problems/xavier-initialization |
| Implement z-Score Standardization | Standardize NumPy features to zero mean and unit variance with explicit handling for constant columns. | https://www.tensortonic.com/problems/zscore-standardization |
| ReLU Activation Function | Implement AlexNet's elementwise ReLU activation, preserving positive values while setting negative values to zero. | https://www.tensortonic.com/research/alexnet/alexnet-relu |
| GAN Discriminator | Implement a GAN discriminator that maps input samples through dense layers to real-versus-fake probabilities. | https://www.tensortonic.com/research/gan/gan-discriminator |
| GAN Generator | Implement a GAN generator that transforms latent noise through learned dense layers into generated samples. | https://www.tensortonic.com/research/gan/gan-generator |
| Candidate Hidden State | Compute the GRU candidate hidden state from the current input and the reset-gated previous hidden state. | https://www.tensortonic.com/research/gru/gru-candidate |
| Complete GRU Cell | Build a complete GRU cell with reset and update gates, candidate computation, and the final hidden-state update. | https://www.tensortonic.com/research/gru/gru-cell |
| Hidden State Update | Implement the GRU hidden-state interpolation between the previous state and candidate using the update gate. | https://www.tensortonic.com/research/gru/gru-hidden-update |
| Reset Gate | Implement a GRU reset gate that controls how much of the previous hidden state contributes to the candidate state. | https://www.tensortonic.com/research/gru/gru-reset-gate |
| Update Gate | Implement a GRU update gate that balances retained hidden memory against the new candidate representation. | https://www.tensortonic.com/research/gru/gru-update-gate |
| Complete LSTM Cell | Build a complete LSTM cell with forget, input, candidate, cell-state, output, and hidden-state calculations. | https://www.tensortonic.com/research/lstm/lstm-cell |
| Cell State Update | Implement the LSTM cell-state update by combining retained memory with input-gated candidate information. | https://www.tensortonic.com/research/lstm/lstm-cell-state |
| Forget Gate | Implement an LSTM forget gate by combining the previous hidden state and current input with a sigmoid projection. | https://www.tensortonic.com/research/lstm/lstm-forget-gate |
| Input Gate | Implement the LSTM input gate and candidate activation that control new information written to the cell state. | https://www.tensortonic.com/research/lstm/lstm-input-gate |
| Output Gate | Implement the LSTM output gate and expose the current hidden state from the updated cell memory. | https://www.tensortonic.com/research/lstm/lstm-output-gate |
| Bottleneck Block | Build a ResNet bottleneck block using 1x1 channel reduction, 3x3 convolution, and 1x1 channel expansion. | https://www.tensortonic.com/research/resnet/resnet-bottleneck |
| Convolutional Block | Implement a ResNet convolutional block with a projected shortcut that matches changed spatial and channel dimensions. | https://www.tensortonic.com/research/resnet/resnet-conv-block |
| Identity Block | Implement a ResNet identity block with a three-layer bottleneck branch, batch normalization, ReLU, and an unchanged skip path. | https://www.tensortonic.com/research/resnet/resnet-identity-block |
| Skip Connection Analysis | Analyze ResNet skip connections by combining residual and identity tensors and tracking gradient flow through the addition. | https://www.tensortonic.com/research/resnet/resnet-skip-connection |
| RNN Cell | Implement an Elman RNN cell that combines the current input and previous hidden state before applying tanh. | https://www.tensortonic.com/research/rnn/rnn-cell |
| Hidden State | Initialize a vanilla RNN hidden state as a floating-point zero matrix for the requested batch and hidden dimensions. | https://www.tensortonic.com/research/rnn/rnn-hidden-state |
| Embedding Layer | Create PyTorch token embeddings and scale each lookup by the square root of the Transformer model dimension. | https://www.tensortonic.com/research/transformer/transformers-embedding |
| Positional Encoding | Implement sinusoidal Transformer positional encodings in NumPy with alternating sine and cosine dimensions. | https://www.tensortonic.com/research/transformer/transformers-positional-encoding |
| Tokenization | Build a word-level Transformer tokenizer with fixed special-token IDs, sorted vocabulary entries, encoding, and decoding. | https://www.tensortonic.com/research/transformer/transformers-tokenization |
| ReLU | Implement ReLU activation in Triton with contiguous program tiles, branch-free rectification, and masked tails. | https://www.tensortonic.com/study-plans/triton-basics/triton/triton-relu |

View my verified ML profile: [TensorTonic profile](https://www.tensortonic.com/profile/huyngo)
<!-- tensortonic:end -->
