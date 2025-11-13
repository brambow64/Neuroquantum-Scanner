from neuroquantum_platform import NeuroQuantumProcessor

processor = NeuroQuantumProcessor()
your_eeg_data = [0.1, 0.5, -0.2, 0.3]  # voorbeeld
result = processor.process_segment(your_eeg_data)
print(f"Quality: {result.metrics.quality_score:.2f}")
