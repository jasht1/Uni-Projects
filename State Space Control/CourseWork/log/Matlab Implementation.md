
## Issues

### Unexpected Model Results
%%[[2024-12-14]] @ 17:39%%

What i'm seeing when I simulate the model is a an exponentially growing curve.

Currently my parameters are as follows:

```matlab title="QC_params.m"

%% Physical Paramiters
m_b = 150;      % (kg)
m_w = 11;       % (kg)
b_s = 690;      % (N/m/s)
k_s = 6936;     % (N/m)
k_t = 28712;    % (N/m)

if ~exist('f_s', 'var') % make suspension passive if coeficients not defined
  f_s = 0;
end

%% State Space Representation
A = [
  0 1 0 0;
  -k_s/m_b -b_s/m_b k_s/m_b b_s/m_b;
  0 0 0 1;
  k_s/m_w b_s/m_w (k_t-k_s)/m_w -b_s/m_w;
  ];

B = [
  0 0;
  0 f_s/m_b;
  0 0;
  k_t/m_w -f_s/m_w
  ];

C = [0 1 0 0];
D = 0;

plant = ss(A,B,C,D);

```

Which give my A matrix unstable poles. As can be seen the second term of the eigenvalue is positive which explains the runaway feedback. There are also imaginary components in the 3rd and 4th poles but these are of much less effect.

```
A =

   1.0e+03 *

         0    0.0010         0         0
   -0.0462   -0.0046    0.0462    0.0046
         0         0         0    0.0010
    0.6305    0.0627    1.9796   -0.0627

eig(A) =

 -87.9380 + 0.0000i
  26.9788 + 0.0000i
  -3.1840 + 6.3824i
  -3.1840 - 6.3824i
```

Clearly there is an error in the [[Designing State Space Model#State Matrices]]. 
