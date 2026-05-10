import numpy as np

def wasserstein_critic_loss(real_scores, fake_scores):
    """
    Compute Wasserstein Critic Loss for WGAN.
    """
    # Write code here
    fake = np.mean(fake_scores)
    real = np.mean(real_scores)

    return fake - real