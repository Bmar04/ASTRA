import socket
import threading
import time
import json
from typing import Optional, Callable, Tuple

class TcpClient:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.socket = None
        self.is_connected = False
        self.running = False
        self.callback = None
    
    def set_callback(self, callback: Callable):
        self.callback = callback

    def connect(self):
        if not self.callback:
            raise ValueError("Callback not set")

        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            self.is_connected = True
            self.running = True

            thread = threading.Thread(target=self._receive_loop, daemon=True)
            thread.start()

        except Exception as e:
            self.is_connected = False
            raise e

    def start(self):
        """Alias for connect"""
        self.connect()
     
    def stop(self):
        """Stop receiving and disconnect"""
        self.running = False
        if self.socket:
            self.socket.close()
        print("🔌 Disconnected")
     
    def _receive_loop(self):
        """Receive JSON lines from server"""
        buffer = ""
        
        while self.running and self.socket:
            try:
                # Receive data
                data = self.socket.recv(1024).decode('utf-8')
                if not data:
                    break
                
                # Add to buffer and process complete lines
                buffer += data
                lines = buffer.split('\n')
                buffer = lines[-1]  # Keep incomplete line
                
                # Process each complete line
                for line in lines[:-1]:
                    line = line.strip()
                    if line and self.callback:
                        try:
                            json_data = json.loads(line)
                            self.callback(json_data)
                        except json.JSONDecodeError:
                            print(f"⚠️  Bad JSON: {line}")
                            
            except Exception as e:
                print(f"❌ Receive error: {e}")
                break

# Example usage
def example_callback(json_data):
    """Example function to handle received JSON"""
    print(f"📡 {json_data}")

def main():
    """Test the TCP client"""
    print("🌐 Simple TCP Client Test")
    print("Start your CSV parser with: python csv_parser.py data.csv --tcp")
    
    client = TcpClient("localhost", 8080)
    client.set_callback(example_callback)
    client.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        client.stop()

if __name__ == "__main__":
    main()