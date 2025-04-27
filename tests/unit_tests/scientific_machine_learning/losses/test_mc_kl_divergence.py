import pytest
import torch
import torch.nn as nn
from hypothesis import given, settings
from hypothesis import strategies as st

import UQpy.scientific_machine_learning as sml
from UQpy.distributions import Lognormal, Normal

settings.register_profile("fast", max_examples=1)
settings.load_profile("fast")


@given(width=st.integers(min_value=1, max_value=10))
def test_divergence_shape(width):
    network = nn.Sequential(
        sml.BayesianLinear(1, width),
        nn.ReLU(),
        sml.BayesianLinear(width, width),
        nn.ReLU(),
        sml.BayesianLinear(width, 1),
    )
    model = sml.FeedForwardNeuralNetwork(network)
    mc_divergence = sml.MCKullbackLeiblerDivergence(
        posterior_distribution=Normal, prior_distribution=Normal, n_samples=1
    )
    divergence = mc_divergence(model)
    assert divergence.shape == torch.Size()


def test_reduction_none_raises_error():
    with pytest.raises(ValueError):
        sml.MCKullbackLeiblerDivergence(
            posterior_distribution=Normal, prior_distribution=Normal, reduction="none", n_samples=1
        )
