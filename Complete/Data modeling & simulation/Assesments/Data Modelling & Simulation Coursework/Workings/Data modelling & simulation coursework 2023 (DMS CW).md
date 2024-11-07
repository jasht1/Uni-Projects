%%[[Data Modelling & simulation coursework brief.pdf]]%%
# Data modelling & simulation coursework 2023
Joseph Ashton (27047440)
## Question 1
**Suppose you have recorded the displacement y of a point on a vibrating string at various time intervals t, and the data is as follows:**
###### given data
| t (s) | y    |
| ----- | ---- |
| 0     | 0    |
| 0.1   | 0.5  |
| 0.2   | 0.8  |
| 0.3   | 0.6  |
| 0.4   | 0    |
| 0.5   | -0.4 |
| 0.6   | -0.7 |
| 0.7   | -0.5 |
| 0.8   | -0.2 |
| 0.9   | 0.1  |
| 1     | 0.4  |
| 1.1   | 0.2  |
| 1.2   | 0    |
### a) 
**Sketch the waveform based on the given data and construct a Fourier series for the first three harmonics. [10 Marks]**
begin by identifying the key features of the dataset:
- starts at $(0,0)$
- first peak at roughly $(0.2,0.8)$
- crosses x axis at $(0.4,0)$
- First trough at roughly $(0.6,0.7)$
- crosses x axis again at roughly $(0.9,0)$
- next peak at roughly $(1,0.4)$
- crosses x axis again at $(1.2,0)$ 
Then roughly plotting the points and sketching a diminishing sinusoid to fit:
![[DMS CW Q1 function sketch.png]]
Now a numerical model for the behaviour implied by the data can be found.
Given that the pattern appears to be a diminishing sinusoid a good starting point is the general formula for a damped [[Fourier series]] which is:
$$f(x) = a_0 + \sum_{n=1}^\infty \left(a_n\cos \frac{n\pi x}{L} +b_n\sin \frac{n\pi x}{L}\right)e^{-\alpha x}$$
where $L$ is half the period $L = \frac{1}{2} T$, $\alpha$ is the damping coefficient, $a_0$ is the average value over a period and $a_n$ & $b_n$ are coefficients of sine & cosine components they are defined by the Euler formulas: 
$$
a_0 = \frac{1}{2L}\int_{-L}^L f(x)e^{-\alpha x}dx 
\quad \& \quad 
\displaylines{ 
a_n = \frac{1}{L}\int_{-L}^L f(x)\cos (\frac{n\pi x}{L})e^{-\alpha x} dx 
\\
b_n = \frac{1}{L}\int_{-L}^L f(x)\sin (\frac{n\pi x}{L})e^{-\alpha x} dx
}
$$
The period $T$ can be approximated as $T = 0.8$ as there are one and a half oscillations in 1.2 seconds, making $L =0.4$.
The damping coefficient $\alpha$ is related to the half life by $\alpha=\frac{ln(2)}{T_{half}​}​$. Given that the second peak is half the amplitude as the first, $(1,0.4)$ & $(0.2,0.8)$ respectively, the half life can be assumed to be equal to the period $T_{half}​=T=0.8$. This would make $\alpha=\frac{ln(2)}{0.8​}​ \approx 0.866$.
The Average amplitude $a_0$ can be approximated as $0$ as without damping the system would be perfectly sinusoidal with each period having a net area of $0$.
The Fourier coefficient $a_n$ determines the effect of the cosine component and given that the function begins at $(0,0)$ it can be assumed to be $0$.
$b_n$ can be found by taking into account the previously estimated period & decay constant and approximating the undamped amplitude $f(x)$ based on the peaks & troughs divided by the damping at that point like so $f(x) = \frac{y}{e^{-\alpha x}}$. Using this formula at the 3 peaks gives $[0.95, 1.18, 0.95]$ respectively so $f(x) \approx 1$ and can be ignored giving:
$$b_n = \frac{1}{0.4}\int_{0}^{0.4} \sin (\frac{n\pi x}{0.4})e^{-\frac{ln(2)}{0.8} x} dx$$
### b) 
**Plot the original waveform and Fourier series (N=3) in MATLAB [10 Marks]**
#### MATLAB Code
``` python
clear close all

%% Defined Variables

x = 0:0.1:1.2;
y = [0, 0.5, 0.8, 0.6, 0, -0.4, -0.7, -0.5, -0.2, 0.1, 0.4, 0.2, 0];

n_max = 3; % number of Fourier terms
  
%% Estimated variable functions
  
T = x(end) - x(1);
a0 = (1/T) * trapz(x, y);
an = zeros(1, n_max);
bn = zeros(1, n_max);
  
for n = 1:n_max
	an(n) = (2/T) * trapz(x, y .* cos(2*pi*n*x/T));
	bn(n) = (2/T) * trapz(x, y .* sin(2*pi*n*x/T));
end

%% find Fourier series
  
t = linspace(x(1), x(end), 1000);
ft = a0/2;
for n = 1:n_max
	ft = ft + an(n) * cos(2*pi*n*t/T) + bn(n) * sin(2*pi*n*t/T);
end

%% original data vs Fourier series plot
  
figure;
	scatter(x, y, 'o', 'DisplayName', 'Original Data');
	hold on;
	plot(t, ft, 'r-', 'DisplayName', 'Estimated Fourier Series');
	legend('show');
	title('Estimated Fourier Series');
	xlabel('Time');
	ylabel('displacement');
	grid on;
```
#### Output
![[Estimated fourier series.svg]]

### c) 
**Plot the 3th (N=3) and 6th (N=6) Fourier series in MATLAB in one figure and compare the results [10 Marks]**
#### MATLAB Code
``` python
clear close all

%% Defined Variables

x = 0:0.1:1.2;
y = [0, 0.5, 0.8, 0.6, 0, -0.4, -0.7, -0.5, -0.2, 0.1, 0.4, 0.2, 0];
n_1ow = 3; % Lower number of Fourier terms
n_max = 6; % Highest number of Fourier terms
  
%% Estimated variable functions

T = x(end) - x(1);
a0 = (1/T) * trapz(x, y);
an = zeros(1, n_max);
bn = zeros(1, n_max);
  
for n = 1:n_max
	an(n) = (2/T) * trapz(x, y .* cos(2*pi*n*x/T));
	bn(n) = (2/T) * trapz(x, y .* sin(2*pi*n*x/T));
end
  
%% find Fourier series

ftl = a0/2; fth = a0/2;
t = linspace(x(1), x(end), 1000);
  
for n = 1:n_1ow
	ftl = ftl + an(n) * cos(2*pi*n*t/T) + bn(n) * sin(2*pi*n*t/T);
end
for n = 1:n_max
	fth = fth + an(n) * cos(2*pi*n*t/T) + bn(n) * sin(2*pi*n*t/T);
end
  
%% original data vs Fourier series plot

figure;
	scatter(x, y, 'o', 'DisplayName', 'Original Data');
	hold on;
	plot(t, ftl, 'b', 'DisplayName', 'n = 3');
	hold on;
	plot(t, fth, 'r-', 'DisplayName', 'n = 6');
	legend('show');
	title('3 vs 6 Term Fourier Series');
	xlabel('Time');
	ylabel('displacement');
	grid on;
```
#### Output
![[3vs6TermFourierSeries.svg]]

## Question 2
**Consider the function $𝑓(𝑥) = 𝑥^2$ on the interval $0 ≤ 𝑥 ≤ 1$.** 
### a) 
**Find the even and odd extension Fourier series of 𝑓(𝑥) [15 Marks]**
To find the even & odd extensions of this function the interval considered must be extended form $0 ≤ 𝑥 ≤ 1$ to $-1 ≤ 𝑥 ≤ 1$. This will be different for the even & for the odd case as you can see by this diagram:
![[even vs odd function diagram.png]]
Therefore this answer will split into 2 sections; the first will find the even extension by assuming the function is mirrored about the y axis, and then in the next section the odd case will be considered where it is not.
#### Even Extension
The even case $f_e$ is defined by the statement $f(x) = f(-x)$,
$$ f_{e}(x) = \begin{cases}
f(-x) & - 1 ≤ x ≤ 0 \\
f(x) & 0≤ x≤ 1
\end{cases}$$
$x^2$ is an even function as $(x)^2 = (-x)^2$, so we will simplify down to $𝑓_e(𝑥) = 𝑥^2$ in the interval $-1 ≤ 𝑥 ≤ 1$.
Now a Fourier series can be constructed for this case where the Fourier coefficients needed are $a_0$ and $a_n$,the $b_n$ term evaluates to 0 as there are no sine terms needed in even functions. The relevant formulas being:
$$
\displaylines{ 
a_0 = \frac{1}{2L}\int_{-L}^L f(x)dx 
\\
a_n = \frac{1}{L}\int_{-L}^L f(x)\cos \frac{n\pi x}{L} dx 
}
$$
As in this case the limits $L = 1$ and $𝑓(𝑥) = 𝑥^2$ simplifying the equations to:

$$
\displaylines{ 
a_0 = \frac{1}{2}\int_{-1}^1 x^2dx 
\\
a_n = \int_{-1}^1 x^2\cos (n\pi x) \ dx 
}
$$
And then substituting these into the general Fourier series the even series can be defined as:
$$ f(x) = \frac{1}{4}\int_{-1}^1 x^2dx + \sum_{n=1}^{\infty} \left[ \int_{-1}^1 x^2 \cos(n\pi x) \, dx \cdot \cos\left(\frac{n\pi x}{1}\right) \right] $$
#### Odd case
The odd case $f_o$ is defined by the statement $f(x) = -f(x)$,
$$ f_{e}(x) = \begin{cases}
-f(-x) & - 1 ≤ x ≤ 0 \\
f(x) & 0≤ x≤ 1
\end{cases}$$
In this case the $a_0$ & $a_n$ coefficients are not needed as the net area will be 0 & no sines are used. The only coefficient needed is: 
$$b_n = \frac{1}{L}\int_{-L}^L f(x)\sin \frac{n\pi x}{L} dx $$
substituting in known values as:
$$ b_n = \int_{-1}^1 x^2\sin (n\pi x) \ dx $$
And then constructing the odd Fourier series:
$$
f(x) = \sum_{n=1}^{\infty} \left[ \int_{-1}^1 x^2 \sin(n\pi x) \, dx \cdot \sin\left(\frac{n\pi x}{1}\right) \right]
$$
### b) 
**Plot the even and odd extension Fourier series (even and odd) of 𝑓(𝑥) in MATLAB [10 Marks]**
#### MATLAB code
``` python
%% Qestion 2b
clear
%% Def variables
L = 1; % Length of the interval
x = linspace(-1, L, 1000); % set resoloution
f = @(x) x.^2; % function
N = 10; % num of terms 
a0 = 1/L * integral(@(x) f(x), 0, L);
a_n = zeros(1, N); % even coefficent
b_n = zeros(1, N); % odd coeficient
for n = 1:N 
    % evaluate a_n
    a_n(n) = 2/L * integral(@(x) f(x) .* cos(n * pi * x / L), 0, L);
    % evaluate b_n
    b_n(n) = 2/L * integral(@(x) f(x) .* sin(n * pi * x / L), 0, L);
end

%% Plots
figure;
    % Original function
    subplot(3, 1, 1);
        % plot origional function in given interval
        plot(x(x >= 0), f(x(x >= 0)), 'b-', 'LineWidth', 2);
        hold on
        % plot exact odd extension
        plot(x(x <= 0), -flipud(f(x(x <= 0))), 'g--', 'LineWidth', 2);
        hold on
        % plot exact even extension
        plot(x(x <= 0), f(x(x <= 0)), 'r--', 'LineWidth', 2);
        title('Original Function f(x) = x^2');
        xlabel('x');
        ylabel('f(x)');
        grid on;
        legend({'Even Extension','Odd Extension', 'Original Function'},'Location', 'southeast');
    % Even extension Fourier series
    subplot(3, 1, 2);
        f_even = zeros(size(x));
        f_even = f_even + a0; % a0 needs to be acocunted for in even extension
        for n = 1:N
            f_even = f_even + a_n(n) * cos(n * pi * x / L);
        end
        plot(x, f_even, 'r-', 'LineWidth', 2);
        title('Even Extension Fourier Series');
        xlabel('x');
        ylabel('f_{even}(x)');
        grid on;
    % Odd extension Fourier series
    subplot(3, 1, 3);
        f_odd = zeros(size(x));
        for n = 1:N
            f_odd = f_odd + b_n(n) * sin(n * pi * x / L);
        end
        plot(x, f_odd, 'g-', 'LineWidth', 2);
        title('Odd Extension Fourier Series');
        xlabel('x');
        ylabel('f_{odd}(x)');
        grid on;
    hold off
```
#### Output
![[Q2b even & odd extension plot.png]]

## Question 3
**In some electrical circuits and converters, it is often noticed that the current exhibits a behaviour that resembles the function 𝑓(𝑥), with
$$f(x) = \begin{cases}
0 & - \pi ≤ x ≤ 0 \\
\sin x & 0≤ x≤ \pi
\end{cases} \qquad f(x+2\pi) = f(x)$$
Using the [[Fourier series]] of $f(x)$ Prove that
$$ S = \sum^{\infty}_{n=1} \frac{(-1)^{n+1}} {(2n-1)(2n+1)} = \frac{\pi-2} {4}$$
[15 Marks]**
To create a Fourier series for $f(x)$ the coefficients $a_0$,  $a_n$, & $b_n$ will be found.
$$a_0 = \frac{1}{2\pi}\int_{-\pi}^\pi f(x)dx \quad \& \quad \displaylines{ a_n = \frac{1}{\pi}\int_{-\pi}^\pi f(x)\cos (nx) dx \\ b_n = \frac{1}{\pi}\int_{-\pi}^\pi f(x)\sin (nx) dx}$$
In this case values $≤0$ can be ignored as they have height 0 and therefore contribute 0 area. Given this $a_0$,  $a_n$, & $b_n$  can be found as:
$$
a_0 = \frac{1}{\pi} \int _0 ^\pi sin(x) dx
\quad \& \quad \displaylines{ 
a_n = \frac{2}{\pi}\int_0^\pi \sin(x)\cos (nx) dx \\ 
b_n = \frac{2}{\pi}\int_0^\pi \sin(x)\sin (nx) dx
}$$
Solving / simplifying these equations as follows:
Given that $\int_{0}^{\pi} \sin(x) \, dx = -\cos(x) \Big|_{0}^{\pi} = -\cos(\pi) + \cos(0) = 2$, $a_0$ is found as:
$$ a_0 = \frac{1}{\pi} \int _0 ^\pi sin(x) dx = \frac{1}{\pi} \times 2 = \frac{2}{\pi} $$
Therefore $a_0 = \frac{2}{\pi}$.
The trig identity $sin(x) cos(y) = \frac{1}{2}(sin(x + y) + sin(x - y))$ is used to find
$$
a_n = \frac{2}{\pi}\int_0^\pi \sin(x)\cos (nx) dx =
\frac{2}{\pi}\int_0^\pi \frac{1}{2}(sin(x + nx) + sin(x - nx))dx$$
Allowing the integral $\int_0^\pi \frac{1}{2}(sin(x + nx) + sin(x - nx))dx$ to be split in two giving:
$$\frac{2}{2\pi}\int_0^\pi sin(x + nx)dx + \frac{2}{2\pi}\int_0^\pi sin(x - nx)dx$$
Focusing on the first integral using the anti-derivative $\int sin(ax)dx = -\frac 1 a ​cos(ax)$ where $a$ is $(1+n)$,
$$\int_0^\pi sin((1+n)x)dx =
-\frac{1}{1+n}\cos((1+n)x) \Big|_{0}^{\pi} $$
Then evaluating the limits observing that $cos((1\pm n)\pi) = -cos(n\pi)$,
$$\frac{1}{1+n}(\cos(0) - \cos((1+n)\pi)) = \frac{1}{1+n}(1 + \cos(n\pi)) = \frac{1 + \cos(n\pi)}{1+n}$$
moving on to the second integral using a similar process,
$$\int_0^\pi sin((1-n)x)dx =
-\frac{1}{1-n}\cos((1-n)x) \Big|_{0}^{\pi} $$
$$\frac{1}{1-n}(\cos(0) - \cos((1-n)\pi)) = \frac{1}{1-n}(1 + \cos(n\pi)) = \frac{1 + \cos(n\pi)}{1+n}$$
Substituting these gives $a_n$ as:
$$a_n = 2\left(\frac{2}{2\pi} \times\frac{1 + \cos(n\pi)}{1+n} \right) = \frac{2 + 2\cos(n\pi)}{\pi+n\pi}$$
Now finding $b_n$ using the trig identity $sin(x) sin(y) = \frac{1}{2}(cos(x - y) - cos(x + y))$ 
$$b_n = \frac{2}{\pi}\int_0^\pi \sin(x)\sin (nx) dx = \frac{2}{\pi}\int_0^\pi \frac{1}{2}(cos(x - nx) - cos(x + nx))dx$$
$$b_n =\frac{1}{\pi}\int_0^\pi cos((1 - n)x)dx - \frac{1}{\pi}\int_0^\pi cos((1 + n)x)dx$$
$$b_n = \frac{1}{\pi} \left( \frac{1}{1-n}\sin((1-n)x) \Big|_{0}^{\pi}  \right) - \frac{1}{\pi} \left( \frac{1}{1+n}\sin((1+n)x) \Big|_{0}^{\pi}  \right)$$
Noting that $sin(n\pi) = 0$ both limits will evaluate to 0 therefore $b_n = 0$.
Substituting $a_0$, $a_n$, & $b_n$ into the Fourier series formula,
$$f(x) = \frac{2}{\pi} + \sum_{n=1}^{\infty} \left(\frac{2 + 2\cos(n\pi)}{\pi+n\pi}\cos nx\right)$$
Now we have identified the Fourier series it can be used to find the given series. Starting with the identity of $a_n$ which most closely resembles the series.
The component $\cos(n\pi)$ flips between 1 & -1 depending on whether $n$ is even or odd respectively it can therefore be replaced by the component $(-1)^n$ as seen in the given series.
$$a_n =\sum_{n=1}^{\infty} \left(\frac{2 + 2(-1)^n}{\pi+n\pi}\right)$$
the denominator term $\pi+n\pi$ can be factored into $(1+n)\pi$,
$$a_n =\sum_{n=1}^{\infty} \left(\frac{2 + 2(-1)^n}{(1+n)\pi}\right)$$
This allows for $\frac{2}{\pi}$ to be factored out of the summation,
$$a_n =\frac{2}{\pi} \sum_{n=1}^{\infty} \left(\frac{1 + (-1)^n}{1+n}\right)$$
Further to this $\frac{1}{1+n}$ can be separated into its own summation,
$$a_n =\frac{2}{\pi} \sum_{n=1}^{\infty} \left( \frac{1}{1+n} \right) + \frac{2}{\pi} \sum_{n=1}^{\infty} \left(\frac{(-1)^n}{1+n}\right)$$
The second summation can be split into its even and odd components,
$$a_n =\frac{2}{\pi} \sum_{n=1}^{\infty} \left( \frac{1}{1+n} \right) + \frac{2}{2\pi} \sum_{n=1}^{\infty} \left(\frac{(-1)^n}{(2n)+1}+\frac{(-1)^{2n+1}}{(2n+1)+1}\right)$$
The series $S = \sum^{\infty}_{n=1} \frac{(-1)^{n+1}} {(2n-1)(2n+1)}$ can be shown to approach $\frac{\pi-2} {4}$ numerically with the following Matlab code:
### Matlab code
``` js
f = @(n) (-1)^(n+1) / ((2*n-1)*(2*n+1));
% Define the number of terms in the series
N_terms = 20;

% Initialize an array to store partial sums
partial_sums = zeros(1, N_terms);

% Calculate partial sums
for n = 1:N_terms
    partial_sums(n) = sum(arrayfun(f, 1:n));
end

% Plot the partial sums
figure;
stem(1:N_terms, partial_sums, 'LineWidth', 2, 'MarkerSize', 8, 'DisplayName', 'Given series');
hold on 
yline((pi - 2)/4, 'r--', 'LineWidth', 2, 'DisplayName', '(pi - 2)/4');
ylim([0.25, 0.35]);
title(['Partial Sums of the Series with up to ', num2str(N_terms), ' Terms']);
legend
xlabel('Number of Terms');
ylabel('Partial Sum');
grid on;
```
### Output
![[Pasted image 20231218234326.png]]

## Question 4 
Consider the following nonlinear first-order ODE: 
$$2𝑥𝑦^2 + 4 = 2(3 − 𝑦𝑥^2)𝑦'$$
### a) 
**Using the Euler method with three step sizes; $h = 0.1, 0.01,0.001$, approximate the solution $y(t)$ over the time interval $[-1, 2]$ with an initial condition $y (-1) = 8$. Implement this numerical solution using MATLAB. [10 Marks]** 
The provided ODE can be simply rearranged to make $y'$ the subject by dividing both sides by $2(3-yx^2)$ to make:
$$y'=\frac{xy^2+2}{3-yx^2}$$
This can now be used in the following Matlab script:
``` python
% definitions
f = @(x, y) (2 * x * y^2 + 4) / (2 * (3 - y * x^2));% the ODE function
tspan = [-1, 2];% Time interval
x0 = -1; y0 = 8;% Initial conditions
h_values = [0.1, 0.01, 0.001];% Step sizes

% Plotting
figure;
for h = h_values
    % arrays to log results
    x_values = x0:h:tspan(2);
    y_values = zeros(size(x_values));
    
    % Set initial condition
    x_values(1) = x0;
    y_values(1) = y0;
    
    % Euler method
    for i = 1:length(x_values)-1
        y_prime = f(x_values(i), y_values(i));
        y_values(i+1) = y_values(i) + h * y_prime;
    end

    % Plot the result
    subplot(3, 1, find(h_values == h));
    plot(x_values, y_values, 'o-', 'DisplayName', ['h = ' num2str(h)]);
    % Labels
    xlabel('t');
    ylabel('y(t)');
    title(['Euler Method for h = ' num2str(h)]);
end
legend('Location', 'Bestoutside');
```
### b) 
**Plot the numerical solution $y(t)$ obtained from the Euler method for different step size. Include appropriate labels on the plot. [10 Marks]** 
Plotting these approximations shows large spikes around 0. With a step size of 0.1 a large negative spike appears just after 0 and returns back towards the x axis. However on the finer step sizes this negative portion is made unsolvable by the peak at 0.
![[Pasted image 20231215230625.png]]
The rest of the shape can be observed more clearly if plotted without the impulse at 0 as seen below:
![[Q4b-without-impulse.jpg]]
This shape forms a classic reciprocal function it rapidly increases just as it approaches 0 and then immediately after 0 jumps negative and rapidly but decreasing approaches 0 from the other side.
### c) 
**Compare the results of three step sizes with exact solution. Note that the exact solution can be determined analytically as: 
$$𝑦 = \frac{3 + \sqrt{−4𝑥^2(𝑥 − 3) + 9}} {𝑥^2}$$
[10 Marks]**
Plotting the analytical solution with the following Matlab script:
``` js
x = linspace(-1,2,100);
Es = (3 + sqrt((-4 * x.^2 .* (x - 3) + 9))) ./ x.^2;
figure;
	plot(x, Es, 'b', 'DisplayName', 'Exact Solution');
	xlabel('x');
	ylabel('y');
	title('Exact Solution');
	grid on;
	legend('Location', 'northeast');
```
results in the graph below.
###### Exact solution plot
![[Q4c-exact-solution.png]]
The rate / width of the impulse is effectively identical to those found by Euler's method. However it obviously differs from plots produced using Euler's method in Matlab as it remains positive.
I briefly considered that the previous method had found the differential of function plotted in [[#Exact solution plot]] as its steep climb to infinity & inversion could potentially be the slope of an impulse. This idea was quickly dismissed by plotting a double integral as well as $y'$ for comparison;
![[Q4c Euler double integral plot.png]]
![[Q4c Euler y' plot.png]]
Clearly this was not the case. It dose however stand to reason that Euler's method would fail after a singularity like this as it assumes local coherence of the function between its steps. It may be possible to make a better approximation with a Runge-Kutta style method but all numerical approximations which rely on local coherence will struggle with singularities and other discontinuities.
# Annexes
## Full matlab code
``` js
Data modelling & simulation coursework code

Question 1
%%## Question 1a
clear

%% Defined Variables
x = 0:0.1:1.2;
y = [0, 0.5, 0.8, 0.6, 0, -0.4, -0.7, -0.5, -0.2, 0.1, 0.4, 0.2, 0];

n_max = 3; % number of Fourier terms

%% Estimated variable functions
T = x(end) - x(1);
a0 = (1/T) * trapz(x, y);
an = zeros(1, n_max);
bn = zeros(1, n_max);

for n = 1:n_max
	an(n) = (2/T) * trapz(x, y .* cos(2*pi*n*x/T));
	bn(n) = (2/T) * trapz(x, y .* sin(2*pi*n*x/T));
end
  
%% find Fourier series

t = linspace(x(1), x(end), 1000); % create a finer time vector for plotting
ft = a0/2;
for n = 1:n_max
	ft = ft + an(n) * cos(2*pi*n*t/T) + bn(n) * sin(2*pi*n*t/T);
end
  
%% original data vs Fourier series plot

figure;
	scatter(x, y, 'o', 'DisplayName', 'Original Data');
	hold on;
	plot(t, ft, 'r-', 'DisplayName', 'Estimated Fourier Series');
	legend('show');
	title('Estimated Fourier Series');
	xlabel('Time');
	ylabel('displacement');
	grid on;

%%## Question 1b
clear
%% Defined Variables
x = 0:0.1:1.2;
y = [0, 0.5, 0.8, 0.6, 0, -0.4, -0.7, -0.5, -0.2, 0.1, 0.4, 0.2, 0];
n_1ow = 3; % Lower number of Fourier terms
n_max = 6; % Highest number of Fourier terms

%% Estimated variable functions
T = x(end) - x(1);
a0 = (1/T) * trapz(x, y);
an = zeros(1, n_max);
bn = zeros(1, n_max);

for n = 1:n_max
    an(n) = (2/T) * trapz(x, y .* cos(2*pi*n*x/T));
    bn(n) = (2/T) * trapz(x, y .* sin(2*pi*n*x/T));
end

%% find Fourier series
ftl = a0/2; fth = a0/2;
t = linspace(x(1), x(end), 1000); % create a finer time vector for plotting

for n = 1:n_1ow
    ftl = ftl + an(n) * cos(2*pi*n*t/T) + bn(n) * sin(2*pi*n*t/T);
end
for n = 1:n_max
    fth = fth + an(n) * cos(2*pi*n*t/T) + bn(n) * sin(2*pi*n*t/T);
end

%% original data vs Fourier series plot
figure;
scatter(x, y, 'o', 'DisplayName', 'Original Data');
hold on;
plot(t, ftl, 'b', 'DisplayName', 'n = 3');
hold on;
plot(t, fth, 'r-', 'DisplayName', 'n = 6');
legend('show');
title('3 vs 6 Term Fourier Series');
xlabel('Time');
ylabel('displacement');
grid on;
%%% my aprox function plot
clear

Data_x = 0:0.1:1.2;
Data_y = [0, 0.5, 0.8, 0.6, 0, -0.4, -0.7, -0.5, -0.2, 0.1, 0.4, 0.2, 0];

syms x;
n = 1;
T = 0.8;
L = T/2;
a0 = 0;
an = 0;
alpha = log(2) / T;

% Calculate bn terms and damped Fourier series expression
f_x = a0;
for n_val = 1:n
    bn = 1;%(2 / L) * int(x^2 * sin(n_val * pi * x / L) * exp(-alpha * x), 0, L);
    f_x = f_x + (bn * sin(n_val * pi * x / L)) * exp(-alpha * x);
end

% Plotting
figure;
fplot(f_x, [0, 1.2]);
hold on
scatter(Data_x, Data_y, 'o', 'DisplayName', 'Original Data');
title('Damped Fourier Series Plot');
xlabel('x');
ylabel('f(x)');
grid on;

Question 2
%% Qestion 2b
clear
%% Def variables
L = 1; % Length of the interval
x = linspace(-1, L, 1000); % set resoloution
f = @(x) x.^2; % function
N = 10; % num of terms 
a0 = 1/L * integral(@(x) f(x), 0, L);
a_n = zeros(1, N); % even coefficent
b_n = zeros(1, N); % odd coeficient
for n = 1:N 
    % evaluate a_n
    a_n(n) = 2/L * integral(@(x) f(x) .* cos(n * pi * x / L), 0, L);
    % evaluate b_n
    b_n(n) = 2/L * integral(@(x) f(x) .* sin(n * pi * x / L), 0, L);
end

%% Plots
figure;
    % Original function
    subplot(3, 1, 1);
        % plot origional function in given interval
        plot(x(x >= 0), f(x(x >= 0)), 'b-', 'LineWidth', 2);
        hold on
        % plot exact odd extension
        plot(x(x <= 0), -flipud(f(x(x <= 0))), 'g--', 'LineWidth', 2);
        hold on
        % plot exact even extension
        plot(x(x <= 0), f(x(x <= 0)), 'r--', 'LineWidth', 2);
        title('Original Function f(x) = x^2');
        xlabel('x');
        ylabel('f(x)');
        grid on;
        legend({'Even Extension','Odd Extension', 'Original Function'},'Location', 'southeast');
    % Even extension Fourier series
    subplot(3, 1, 2);
        f_even = zeros(size(x));
        f_even = f_even + a0; % a0 needs to be acocunted for in even extension
        for n = 1:N
            f_even = f_even + a_n(n) * cos(n * pi * x / L);
        end
        plot(x, f_even, 'r-', 'LineWidth', 2);
        title('Even Extension Fourier Series');
        xlabel('x');
        ylabel('f_{even}(x)');
        grid on;
    % Odd extension Fourier series
    subplot(3, 1, 3);
        f_odd = zeros(size(x));
        for n = 1:N
            f_odd = f_odd + b_n(n) * sin(n * pi * x / L);
        end
        plot(x, f_odd, 'g-', 'LineWidth', 2);
        title('Odd Extension Fourier Series');
        xlabel('x');
        ylabel('f_{odd}(x)');
        grid on;
    hold off

question 3
clear
% definitions
syms x;% Symbolic variable
f = piecewise(-pi <= x < 0, 0, 0 <= x <= pi, sin(x));% Define the piecewise function
T = 2*pi;% Period of the function
a0 =(1/T) * int(f, -pi, pi);% Calculate a_0  2/pi;%
n = 5;% Number of terms in the Fourier series

% Initialize coefficients
an = zeros(1, n);
bn = zeros(1, n);

% Calculate a_n and b_n terms
for n = 1:n
    an(n) = (1/pi) * int(f * cos(n*x), -pi, pi);
    bn(n) = (1/pi) * int(f * sin(n*x), -pi, pi);
end

% Construct Fourier series
f_fourier = a0;
for n = 1:n
    f_fourier = f_fourier + an(n) * cos(n*x) + bn(n) * sin(n*x);
end

% Plotting
figure;
    fplot(f, [-pi, pi], 'DisplayName', 'Original Function');
    hold on
    fplot(f_fourier, [-pi, pi], 'r--', 'DisplayName', 'Fourier Series');
    title('Fourier Series for f(x)');
    xlabel('x');
    ylabel('f(x)');
    legend('Location', 'northwest');
    grid on;
    hold off;

plot my series
clear
% Define the function f(x)
f = @(x, N) (2/pi) + sum((2 + 2*cos(pi*(1:N)))./(pi + pi*(1:N)) .* cos((1:N)' .* x), 2);
% f = @(x, N) (2/pi) + sum(((-1)^(n+1) / ((2*n-1)*(2*n+1))) .* cos((1:N)' .* x), 2);
% Define the range of x values
x_values = linspace(0, 2*pi, 1000);

% Set the number of terms in the series (adjust as needed)
N_terms = 10;

% Initialize y_values with the constant term
y_values = (2/pi)*ones(size(x_values));

% Calculate the Fourier series terms and update y_values
for n = 1:N_terms
    term = (2 + 2*cos(pi*n))/(pi + pi*n) * cos(n * x_values);
    y_values = y_values + term;
end

% Plot the function
figure;
plot(x_values, y_values, 'LineWidth', 2);
title(['Fourier Series with ', num2str(N_terms), ' Terms']);
xlabel('x');
ylabel('f(x)');
grid on;

plot given funciton

% Define the function for the series
f = @(n) (-1)^(n+1) / ((2*n-1)*(2*n+1));
% f = @(n) (2 + 2*cos(n*pi)) / (pi + n*pi);
% Define the number of terms in the series
N_terms = 20;

% Initialize an array to store partial sums
partial_sums = zeros(1, N_terms);

% Calculate partial sums
for n = 1:N_terms
    partial_sums(n) = sum(arrayfun(f, 1:n));
end

% Plot the partial sums
figure;
stem(1:N_terms, partial_sums, 'LineWidth', 2, 'MarkerSize', 8, 'DisplayName', 'Given series');
hold on 
yline((pi - 2)/4, 'r--', 'LineWidth', 2, 'DisplayName', '(pi - 2)/4');
ylim([0.25, 0.35]);
title(['Partial Sums of the Series with up to ', num2str(N_terms), ' Terms']);
legend
xlabel('Number of Terms');
ylabel('Partial Sum');
grid on;

Question 4
Adjusting k1s code
h = 0.1;   % Step size
x = -1:h:4; % x interval definition
y = zeros(size(x));
y(1) = 8;   % Initial condition
n = numel(y);

dydx = ((x.*y.^2)+2)/(3-y.*x.^2); %@(x, y) (2 * x * y^2 + 4) / (2 * (3 - y * x^2))
% Define the ODE function
for i = 1:n-1
    % Update y using the Euler method
    y(i+1) = y(i) + h * dydx;
end

% Plot the results
figure;
plot(x, y, 'ro', 'DisplayName', 'Euler Method');
hold on;

% Plot the exact solution for comparison
%f1 = (3+sqrt(-4.*x.^2.*(x-3)+9))/x.^2;
%plot(x, f1, 'b', 'DisplayName', 'Exact Solution');
grid on;

% Add labels and legend
xlabel('t');
ylabel('y(t)');
title('Euler Method Approximation vs Exact Solution');
legend('Location', 'Best');

my code
clear
% definitions
f = @(x, y) (2 * x * y^2 + 4) / (2 * (3 - y * x^2));% the ODE function
tspan = [-1, 2];% Time interval
x0 = -1; y0 = 8;% Initial conditions
h_values = [0.1, 0.01, 0.001];% Step sizes

% Plotting
figure;
for h = h_values
    % arrays to log results
    x_values = x0:h:tspan(2);
    y_values = zeros(size(x_values));
    
    % Set initial condition
    x_values(1) = x0;
    y_values(1) = y0;
    
    % Euler method
    for i = 1:length(x_values)-1
        y_prime = f(x_values(i), y_values(i));
        y_values(i+1) = y_values(i) + h * y_prime;
    end

    % Plot the result
    subplot(3, 1, find(h_values == h));
    plot(x_values, y_values, 'o-', 'DisplayName', ['h = ' num2str(h)]);
    % Labels
    xlabel('t');
    ylabel('y(t)');
    title(['Euler Method for h = ' num2str(h)]);
end
legend({'y(t)'},'Location', 'Bestoutside');
set(gcf, 'Position', [100, 100, 800, 800]);

Exact solution
figure;
x = linspace(-1,2,1000);
Es = (3 + sqrt((-4 * x.^2 .* (x - 3) + 9))) ./ x.^2;
plot(x, Es, 'b', 'DisplayName', 'Exact Solution');
xlabel('x');
ylabel('y');
title('Exact Solution');
grid on;
legend('Location', 'northeast');

Going further
Without peak at 0
figure;
for h = h_values
    % Initialize arrays to store results
    x_values = x0:h:tspan(2);
    y_values = zeros(size(x_values));
    
    % Set initial condition
    x_values(1) = x0;
    y_values(1) = y0;
    
    for i = 1:length(x_values)-1
        y_prime = f(x_values(i), y_values(i));
        y_values(i+1) = y_values(i) + h * y_prime;
    end
    
    % Plot the result
    subplot(3, 1, find(h_values == h));
    %plot(x_values, y_values, 'o-', 'DisplayName', ['h = ' num2str(h)]);
    plot(x_values(x_values >= 0.02 | x_values <= -0.01), y_values(x_values >= 0.02 | x_values <= -0.01), 'o-', 'DisplayName', ['h = ' num2str(h)]);
    %ylim([-5, 25]);  % Constrain y-axis to
    hold on;
    
    % Display the legend in the last subplot
    if h == h_values(end)
        legend('Location', 'Best');
    end
    hold off;
    % Label the axes
    xlabel('t');
    ylabel('y(t)');
    title(['Euler Method for h = ' num2str(h)]);
end
legend({'y(t)'},'Location', 'Bestoutside');
set(gcf, 'Position', [100, 100, 800, 800]);

Differentiating
% Definitions
f = @(t, y) (2 * t * y^2 + 4) / (2 * (3 - y * t^2));  % ODE function (y')
tspan = [-1, 2];  % Time interval
x0 = -1; y0 = 8;  % Initial conditions
h_values = [0.1, 0.01, 0.001];  % Step sizes

% Plotting
figure;
for h = h_values(3)
    % Initialize arrays to store results
    t_values = x0:h:tspan(2);
    y_prime_values = zeros(size(t_values));
    
    % Set initial condition
    t_values(1) = x0;
    y_prime_values(1) = f(t_values(1), y0);  % Use the ODE function for initial condition
    
    % Euler method for y' (derivative)
    for i = 1:length(t_values)-1
        y_prime = f(t_values(i), y_prime_values(i));
        y_prime_values(i+1) = y_prime_values(i) + h * y_prime;
    end
    
    % Plot the result
    plot( find(h_values == h));
    plot(t_values(t_values >= 0.002 | t_values <= -0.001), y_prime_values(t_values >= 0.002 | t_values <= -0.001), '-','LineWidth', 2, 'DisplayName', ['h = ' num2str(h)]);
    hold on;
    
    % Display the legend in the last subplot
    if h == h_values(end)
        legend('Location', 'Best');
    end
    
    % Label the axes
    xlabel('t');
    ylabel('y''(t)');
    title(['Euler Method for y''(t) with h = ' num2str(h)]);
end

Integrating
% Definitions
f = @(t, y) (2 * t * y^2 + 4) / (2 * (3 - y * t^2));  % ODE function (y')
tspan = [-1, 1];  % Time interval
x0 = -1; y0 = 8;  % Initial conditions
h_values = [0.1, 0.01, 0.001, 0.00001];  % Step sizes

% Plotting
figure;
for h = h_values(4)
    % Initialize arrays to store results
    t_values = x0:h:tspan(2);
    y_values = zeros(size(t_values));
    z_values = zeros(size(t_values));
    
    % Set initial conditions
    t_values(1) = x0;
    y_values(1) = y0;
    z_values(1) = 0;  % Initial condition for the double integral
    
    % First Euler method for y (integral)
    for i = 1:length(t_values)-1
        y_prime = f(t_values(i), y_values(i));
        y_values(i+1) = y_values(i) + h * y_prime;
    end
    
    % Second Euler method for the double integral (z)
    for i = 1:length(t_values)-1
        z_prime = y_values(i);  % Integrate y to get z'
        z_values(i+1) = z_values(i) + h * z_prime;
    end
    
    % Plot the result
    plot(find(h_values == h));
    plot(t_values, z_values, '-','LineWidth', 2, 'DisplayName', ['h = ' num2str(h)]);
    hold on;
    
    % Display the legend in the last subplot
    if h == h_values(end)
        legend('Location', 'Best');
    end
    
    % Label the axes
    xlabel('t');
    ylabel('z(t) (Double Integral)');
    title(['Euler Method for Double Integral with h = ' num2str(h)]);
end

```
## Brief
![[Data Modelling & simulation coursework brief.pdf]]
## References
![[triglaws & identities.pdf]]
![[Fourier series]]
