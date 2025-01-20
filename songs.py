import librosa
import soundfile as sf
from pedalboard import Pedalboard, Reverb, Compressor, Gain, LowpassFilter, HighpassFilter
import os

def create_bass_boosted(audio, sr):
    """Create a bass-boosted version optimized for YouTube"""
    board = Pedalboard([
        HighpassFilter(cutoff_frequency_hz=60),
        LowpassFilter(cutoff_frequency_hz=200),
        Compressor(threshold_db=-20, ratio=4.0),
        Gain(gain_db=3.0)
    ])
    return board(audio, sr)

def create_slower_soothing(audio, sr):
    """Create a slower, soothing version with enhanced vocals"""
    audio_slow = librosa.effects.time_stretch(audio, rate=0.85)
    
    # Enhanced for vocal clarity
    board = Pedalboard([
        # Compressor for vocal enhancement
        Compressor(
            threshold_db=-20,
            ratio=2.5,
            attack_ms=5.0,
            release_ms=100.0
        ),
        # Boost middle frequencies where vocals sit
        HighpassFilter(cutoff_frequency_hz=200),  # Remove unnecessary low frequencies
        LowpassFilter(cutoff_frequency_hz=8000),  # Keep some air but reduce hiss
        # Gentle reverb that doesn't muddy the vocals
        Reverb(
            room_size=0.6,  # Smaller room size for clearer vocals
            damping=0.4,
            wet_level=0.2,  # Less wet mix for clarity
            dry_level=0.8   # More dry signal for vocal presence
        ),
        # Final gain adjustment
        Gain(gain_db=4.0)  # Boost overall volume
    ])
    return board(audio_slow, sr)

def create_lofi_mix(audio, sr):
    """Create a lo-fi version with enhanced vocals"""
    audio_slow = librosa.effects.time_stretch(audio, rate=0.92)
    
    # Enhanced for vocal clarity while maintaining lo-fi aesthetic
    board = Pedalboard([
        # Vocal enhancement chain
        Compressor(
            threshold_db=-25,
            ratio=2.5,
            attack_ms=10.0,
            release_ms=200.0
        ),
        HighpassFilter(cutoff_frequency_hz=150),  # Clear up low-end mud
        LowpassFilter(cutoff_frequency_hz=7500),  # Lo-fi feel but keep vocals clear
        # Classic lo-fi reverb with adjusted settings
        Reverb(
            room_size=0.8,
            damping=0.2,    # Less damping for brighter vocals
            wet_level=0.4,  # Reduced wet level for clarity
            dry_level=0.7   # Increased dry level for vocal presence
        ),
        # Final gain adjustment
        Gain(gain_db=5.0)  # Boost overall volume
    ])
    return board(audio_slow, sr)

# Rest of the code remains the same...