import psutil
import logging
import platform
import subprocess

logger = logging.getLogger(__name__)

def scan_hardware():
    hardware_info = {
        "cpu": False,
        "gpu": False,
        "tpu": False,
        "raspberry_pi": False
    }

    # Check CPU
    try:
        cpu_count = psutil.cpu_count(logical=True)
        if cpu_count > 0:
            hardware_info["cpu"] = True
    except Exception as e:
        logger.error(f"Error scanning CPU: {e}")

    # Check GPU
    try:
        result = subprocess.run(['nvidia-smi'], capture_output=True, text=True)
        if "NVIDIA-SMI" in result.stdout:
            hardware_info["gpu"] = True
    except Exception as e:
        logger.error(f"Error scanning GPU: {e}")

    # Check TPU (Google Coral USB Accelerator)
    try:
        result = subprocess.run(['tpu_monitor'], capture_output=True, text=True)
        if "TPU Monitor" in result.stdout:
            hardware_info["tpu"] = True
    except Exception as e:
        logger.error(f"Error scanning TPU: {e}")

    # Check Raspberry Pi
    try:
        model = platform.model()
        if "Raspberry Pi" in model:
            hardware_info["raspberry_pi"] = True
    except Exception as e:
        logger.error(f"Error scanning Raspberry Pi: {e}")

    logger.info(f"Hardware detected: {hardware_info}")
    return hardware_info
