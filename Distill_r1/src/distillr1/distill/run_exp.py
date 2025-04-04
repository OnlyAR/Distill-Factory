import os
import sys
import json
from typing import Dict, Any, List, Optional
from ..hparams import ModelArguments, DataArguments, get_infer_args, read_args,get_origin_infer_args
from ..data.loader import get_dataset,get_qa_pairs
from ..extras import logging
from ..api.client import Client,parse_client
from ..api.router import ModelRouter
from ..api.app import run_api
import asyncio
import debugpy
from .distiller import Distiller
logger = logging.get_logger(__name__)
async def run_exp(args: Optional[Dict[str, Any]] = None,max_try=3) -> None:
    """
    Run data loading experiment with given arguments.
    
    Args:
        args (Optional[Dict[str, Any]]): Optional dictionary of arguments to override defaults
    """
    router = run_api()
    model_infos = router.get_model_infos()    
    clients = parse_client(model_infos)
    model_args, data_args, finetuning_args,generating_args,distill_args = get_origin_infer_args(args)
    questions,answers = get_qa_pairs(model_args, data_args)
    distiller = Distiller(distill_args,clients,questions,answers)
    await distiller.distill()
if __name__ == "__main__":
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None
    if loop and loop.is_running():
        task = loop.create_task(run_exp())
    else:
        asyncio.run(run_exp())
