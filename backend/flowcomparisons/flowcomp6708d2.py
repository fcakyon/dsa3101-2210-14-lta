from flow import *
import matplotlib.pyplot as plt

def flow():
    p108 = [x*y for x,y in zip(flow6708()[0],flow6708()[2])]
    p110 = [x*y for x,y in zip(flow6710()[0],flow6710()[2])]
    p208 = [x*y for x,y in zip(flow6708()[1],flow6708()[2])]
    p210 = [x*y for x,y in zip(flow6710()[1],flow6710()[2])]
    return [p108, p110, p208, p210]

if __name__ == "__main__":
    flow()


a = flow6708()[5]
b = flow()[2]


plt.plot(np.linspace(1700, 3000, 24), a, label="6708 dir 2 flow from counting")
plt.plot(np.linspace(1700, 3000, 24), b, label="6708 dir 2 flow from formula")

plt.legend(loc="upper left")


plt.xlabel('time')
plt.ylabel('flow')
plt.show()
