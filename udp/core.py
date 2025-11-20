# core.py

# Imports
import socket

class Custom_UDP:
    def __init__(self):
        self.raw_socket = None

        # Holds options for specifying which packets to keep
        self.receive_options = {
            "src_ip": None,
            "dst_ip": None,
            "src_port": None,
            "dst_port": None,
            "max_len": None,
            "keep_malformed": False
        }
    
    def validate_options(self, options:dict) -> bool:
        """
        Validate the options provided for receiving packets.

        :param options: Dictionary of options to validate
        :return: True if valid, False otherwise
        """
        valid_keys = {"src_ip", "dst_ip", "src_port", "dst_port", "max_len", "keep_malformed"}
        for key in options.keys():
            if key not in valid_keys:
                return False
        
        if options.get("src_ip", None) and not isinstance(options["src_ip"], str) \
        or options.get("dst_ip", None) and not isinstance(options["dst_ip"], str) \
        or options.get("src_port", None) and not isinstance(options["src_port"], int) \
        or options.get("dst_port", None) and not isinstance(options["dst_port"], int) \
        or options.get("max_len", None) and not isinstance(options["max_len"], int) \
        or options.get("keep_malformed", None) and not isinstance(options["keep_malformed"], bool):
            return False
        
        return True
    
    def set_receive_options(self, options:dict) -> bool:
        """
        Set the options for receiving packets.

        :param options: Dictionary of options to set
        :return: True if options are valid and set, False otherwise
        """
        if not self.validate_options(options):
            return False
        
        for key, value in options.items():
            self.receive_options[key] = value
        
        return True

    def create_raw_socket(self) -> socket.socket:
        """
        Create a raw socket to implement our custom UDP protocol over it.

        :return: Socket object
        """
        if (self.raw_socket == None):
            try:
                # Open a raw socket that accepts all incoming UDP packets, but don't bind
                self.raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
                return self.raw_socket
            except PermissionError as pe:
                raise Exception("Custom_UDP->create_socket: Permission denied - Raw sockets require elevated privileges.")
            except Exception as e:
                raise Exception(f"Custom_UDP->create_socket: Failed to create a socket - {str(e)}")
        elif (isinstance(self.raw_socket, socket.socket)):
            return self.raw_socket
        else:
            raise Exception("Custom_UDP->create_socket: Invalid socket object stored.")
    
# TODO: Implement send_packet, receive_packet, close_socket, and make the class enterable

if __name__ == "__main__"  :
    udp = Custom_UDP()
    sock = udp.create_raw_socket()
    print("Socket created:", sock)