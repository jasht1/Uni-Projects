
\begin{longtable}[]{@{}
  >{\raggedright\arraybackslash}p{(\linewidth - 4\tabcolsep) * \real{0.0470}}
  >{\raggedright\arraybackslash}p{(\linewidth - 4\tabcolsep) * \real{0.4133}}
  >{\raggedright\arraybackslash}p{(\linewidth - 4\tabcolsep) * \real{0.5397}}@{}}
\toprule\noalign{}
\begin{minipage}[b]{\linewidth}\raggedright
Model
\end{minipage} & \begin{minipage}[b]{\linewidth}\raggedright
Force-Indentation relationship
\end{minipage} & \begin{minipage}[b]{\linewidth}\raggedright
Scope
\end{minipage} \\
\midrule\noalign{}
\endhead
\bottomrule\noalign{}
\endlastfoot
Hertz & \(F = \frac{4}{3}E' \sqrt{R} \ \omega^{3/2}\) & Hertz model
approximates the shallow indention of two linearly elastic spheres with
infinitesimal strains {[}21{]}, {[}22{]}, {[}23{]}. \\
DMT &
\begin{minipage}[t]{\linewidth}
\begin{equation*}
\begin{aligned}
F &= F_{\text{Hertz}} - F_{\text{det}} \\
\delta &= \frac{a}{2} \ln \left( \frac{R_i + a}{R_i - a} \right)
\end{aligned}
\end{equation*}
\end{minipage}
& Depending on the depth of indentation and the material interaction it
can be important to account electrostatic non contact forces, the
influence of which can be modelled using the Derjaguin approximation for
interaction potential {[}19{]}, {[}23{]}. \\
Fung &
\begin{minipage}[t]{\linewidth}
\begin{equation*}
\begin{aligned}
F = &B\pi \left( \frac{N(a)}{D(a)} \right)
\exp\left[ b \left( \frac{E(a)}{F(a)} \right) \right] \\ \\
N(a) &= a^5 - 15Ra^4 + 75R^2a^3 \\
D(a) &= 5Ra^2 - 50R^2a + 125R^3 \\
E(a) &= a^3 - 15Ra^2 \\
F(a) &= 25R^2a - 125R^3 \\
\end{aligned}
\end{equation*}
\end{minipage}
& An exponential strain energy function based on mechanical testing of
mesentery and arterial tissues, that models the non linear elasticity of
cells {[}22{]}, {[}24{]}. This method is tangebly more precise but
doesn't provide a simple value for young's modulus. \\
\end{longtable}
