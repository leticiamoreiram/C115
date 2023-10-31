 from mininet.topo import Topo

 class MyTopo (Topo):
     "4 switches and 9 hosts"

     def __init__(self):
        "Create topo"

        Topo.__init__(self)

        host1 = self.addHost('h1')
        host2 = self.addHost('h2')
        host3 = self.addHost('h3')
        host4 = self.addHost('h4')
        host5 = self.addHost('h5')
        host6 = self.addHost('h6')
        host7 = self.addHost('h7')
        host8 = self.addHost('h8')
        host9 = self.addHost('h9')

        Switch1 = self.addSwitch('s1')
        Switch2 = self.addSwitch('s2')
        Switch3 = self.addSwitch('s3')
        Switch4 = self.addSwitch('s4')

        self.addLink(host1, Switch1)
        self.addLink(host2, Switch1)
        self.addLink(host3, Switch2)
        self.addLink(host4, Switch2)
        self.addLink(host5, Switch3)
        self.addLink(host6, Switch3)
        self.addLink(host7, Switch4)
        self.addLink(host8, Switch4)
        self.addLink(host9, Switch4)

        self.addLink(Switch1, Switch2)
        self.addLink(Switch2, Switch3)
        self.addLink(Switch3, Switch4)






