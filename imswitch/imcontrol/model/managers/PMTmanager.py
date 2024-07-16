import PyDAQmx as nidaq
import numpy as np

class DetectorManager:
    def __init__(self, device_name='Dev1', ao_channel='ao0'):
        self.device_name = device_name
        self.ao_channel = ao_channel
        self.task_handle = nidaq.TaskHandle()
        self._create_task()

    def _create_task(self):
        nidaq.DAQmxCreateTask("", nidaq.byref(self.task_handle))
        nidaq.DAQmxCreateAOVoltageChan(self.task_handle, f"{self.device_name}/{self.ao_channel}", "",
                                       0.0, 5.0, nidaq.DAQmx_Val_Volts, None)

    def set_voltage(self, voltage):
        """Sets the voltage output on the AO channel."""
        if 0.0 <= voltage <= 5.0:
            nidaq.DAQmxWriteAnalogScalarF64(self.task_handle, True, 10.0, voltage, None)
        else:
            raise ValueError("Voltage must be between 0.0 and 5.0 volts")

    def start(self):
        """Starts the task."""
        nidaq.DAQmxStartTask(self.task_handle)

    def stop(self):
        """Stops the task."""
        nidaq.DAQmxStopTask(self.task_handle)

    def clear(self):
        """Clears the task."""
        nidaq.DAQmxClearTask(self.task_handle)

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.clear()

# Example usage:
if __name__ == "__main__":
    with DetectorManager() as detector:
        detector.start()
        try:
            detector.set_voltage(2.5)  # Set the output voltage to 2.5V
            input("Press Enter to continue...")  # Wait for user input to keep the voltage set
        finally:
            detector.stop()
