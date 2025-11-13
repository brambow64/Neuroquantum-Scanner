import numpy as np
from neuroquantum_platform.core.processor import NeuroQuantumProcessor

def test_processor():
    processor = NeuroQuantumProcessor()
    signal = np.random.randn(1000) * 50
    result = processor.process_segment(signal)
    assert 0.0 <= result.metrics.quality_score <= 1.0
    assert isinstance(result.metrics.snr_db, float)
    print("Test geslaagd!")
