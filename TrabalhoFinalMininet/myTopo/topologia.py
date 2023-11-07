from mininet.topo import Topo

class MyTopo( Topo ):
    def __init__(self):
        "Create custom topo."

        # Initialize topology
        Topo.__init__(self)

        # Add hosts
        host1 = self.addHost('h1')
        host2 = self.addHost('h2')
        host3 = self.addHost('h3')
        host4 = self.addHost('h4')
        host5 = self.addHost('h5')
        host6 = self.addHost('h6')
        host7 = self.addHost('h7')
        host8 = self.addHost('h8')
        host9 = self.addHost('h9')

        # Add switches
        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')
        switch3 = self.addSwitch('s3')
        switch4 = self.addSwitch('s4')

        # Add links
        self.addLink(host1, switch1)
        self.addLink(host2, switch1)
        self.addLink(switch2, switch1)
        self.addLink(host3, switch2)
        self.addLink(host4, switch2)
        self.addLink(switch3, switch2)
        self.addLink(host5, switch3)
        self.addLink(host6, switch3)
        self.addLink(switch4, switch3)
        self.addLink(host7, switch4)
        self.addLink(host8, switch4)
        self.addLink(host9, switch4)

topos = { 'mytopo': ( lambda: MyTopo() ) }
