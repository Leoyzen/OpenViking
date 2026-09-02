# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Resource post-ingest processing modes."""

from typing import Literal

SEMANTIC_AND_VECTORS = "semantic_and_vectors"
VECTORS_ONLY = "vectors_only"
NONE = "none"

ProcessingMode = Literal["semantic_and_vectors", "vectors_only"]
WriteProcessingMode = Literal["semantic_and_vectors", "vectors_only", "none"]
DEFAULT_PROCESSING_MODE: ProcessingMode = SEMANTIC_AND_VECTORS
SUPPORTED_PROCESSING_MODES = frozenset({SEMANTIC_AND_VECTORS, VECTORS_ONLY})
SUPPORTED_WRITE_PROCESSING_MODES = frozenset({SEMANTIC_AND_VECTORS, VECTORS_ONLY, NONE})


def normalize_processing_mode(value: str | None) -> ProcessingMode:
    mode = value or DEFAULT_PROCESSING_MODE
    if mode not in SUPPORTED_PROCESSING_MODES:
        supported = ", ".join(sorted(SUPPORTED_PROCESSING_MODES))
        raise ValueError(f"Invalid processing_mode '{mode}'. Supported values: {supported}")
    return mode  # type: ignore[return-value]


def normalize_write_processing_mode(value: str | None) -> WriteProcessingMode:
    mode = value or DEFAULT_PROCESSING_MODE
    if mode not in SUPPORTED_WRITE_PROCESSING_MODES:
        supported = ", ".join(sorted(SUPPORTED_WRITE_PROCESSING_MODES))
        raise ValueError(f"Invalid processing_mode '{mode}'. Supported values: {supported}")
    return mode  # type: ignore[return-value]
