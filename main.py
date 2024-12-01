import time
import yaml
import logging
from hardware_scanner.scanner import scan_hardware
from core_ai.ai_logic import AILogic
from core_ai.code_generator import CodeGenerator
from core_ai.learning_engine import LearningEngine
from utils.error_handling import ErrorHandler
from utils.self_diagnostics import SelfDiagnostics
from utils.logger import setup_logger

logger = setup_logger()

def load_config(config_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    logger.info(f"Loaded configuration: {config}")
    return config

def main():
    config = load_config('config/config.yaml')
    hardware_info = scan_hardware()
    self_diagnostics = SelfDiagnostics()
    error_handler = ErrorHandler()

    # Initialize core AI modules
    ai_logic = AILogic() if config['modules']['ai_logic_enabled'] else None
    code_generator = CodeGenerator() if config['modules']['code_generator_enabled'] else None
    learning_engine = LearningEngine() if config['modules']['learning_engine_enabled'] else None

    self_diagnostics.run_diagnostics(hardware_info)

    while True:
        try:
            # Simulate data processing
            data = "Sample data"
            if ai_logic:
                processed_data = ai_logic.process(data)
            if code_generator:
                generated_code = code_generator.generate_code()
            if learning_engine:
                learned_data = learning_engine.learn(data)
            
            time.sleep(config['self_scan_interval'])
        except Exception as e:
            error_handler.handle_error(e)

if __name__ == "__main__":
    main()
