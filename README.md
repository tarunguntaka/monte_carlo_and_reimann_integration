# monte_carlo_and_reimann_integration
implementation of monte_carlo and reimann integration in python


This a code which takes the integration ideas from monte carlo and reimann and finally display the error 


Monte carlo:
In order to integrate a function over a complicated domain D, Monte Carlo integration picks random points over some simple domain D^' which is a superset of D, checks whether each point is within  D, and estimates the area of D (volume,  n-dimensional content, etc.) as the area of D^' multiplied by the fraction of points falling within D. Monte Carlo integration is implemented in the Wolfram Language as NIntegrate[f, ..., Method -> MonteCarlo].

Picking N randomly distributed points x_1, x_2, ..., x_N in a multidimensional volume V to determine the integral of a function  f in this volume gives a result

 intfdV approx V<f>+/-Vsqrt((<f^2>-<f>^2)/N), 	
(1)
where

<f>	=	1/Nsum_(i=1)^(N)f(x_i)	
(2)
<f^2>	=	1/Nsum_(i=1)^(N)f^2(x_i)	
(3)



Reimann integration:





















