import sys
import argparse

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import math
import random

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--mean", help="Mean/loc of gaussian distribution",
                        default=0)
    parser.add_argument("--variance",
                        help="variance of gaussian distribution",
                        default=2)

   

    args = parser.parse_args()
    mu = args.mean
    v = args.variance
    sigma = math.sqrt(v)

    fig, ax = plt.subplots()
    
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    pdf=norm.pdf(x, mu, sigma)
    ax.plot(x, pdf, color="red")

    print("Probability a<=x<=b")
    st=""
    x=[round(i) for i in x]
    for i in np.unique(x):
        st+=str(round(i))+" "

    print(st)
    a=int(input("a="))
    b=int(input("b="))
    px=np.arange(a,b,0.01)
    ax.fill_between(px,norm.pdf(px, mu, sigma),alpha=0.5, color='g')
    p=norm(mu, sigma).cdf(b) - norm(mu, sigma).cdf(a)
    ax.text(-0.5,0.02,round(p,2), fontsize=20)

    plt.show()

if __name__=="__main__":
    main(sys.argv)

