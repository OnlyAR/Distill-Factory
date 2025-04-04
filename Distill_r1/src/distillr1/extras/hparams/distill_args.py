from dataclasses import asdict, dataclass, field
from typing import Any, Dict, Optional


@dataclass
class ReasoningCurationArguments:
    r"""
    """
    # TODO

@dataclass
class ResponseCurationArguments:
    r"""
    """
    # TODO

@dataclass
class CurationArguments(ReasoningCurationArguments,ResponseCurationArguments):
    """
    Arguments for the synthetic data curation.
    TODO
    """
    pass

@dataclass
class DistillArguments(CurationArguments):
    """
    Arguments for the synthetic data generation.
    """
    method: str = field(
        default="basic",
        metadata={"help": "Method to generate synthetic data.(Reasoning? ... )"},
    )
    output_dir: str = field(
        default="output",
        metadata={"help": "The output directory where the synthetic dataset will be written."},
    )
    output_path: Optional[str] = field(
        default="./synthetic_dataset.json",
        metadata={"help": "The output path where the synthetic dataset will be written."},
    )
    meta_prompt: Optional[str] = field(
        default="",
        metadata={"help": "The meta prompt for the synthetic dataset."},
    )
    enable_reward_model: Optional[bool] = field(
        default=True,
        metadata={"help": "Whether or not to enable reward model."},
    )
    roll_out_size: Optional[int] = field(
        default=1,
        metadata={"help": "The number of roll outs for synthetic data generation."},
    )