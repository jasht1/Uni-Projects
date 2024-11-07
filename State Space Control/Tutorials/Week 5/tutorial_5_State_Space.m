
%%% Time Response

t=0:0.01:10;
wn=2;
zeta=0.1:0.1:0.8;
figure
for i=1:numel(zeta)
  phi=atan2(zeta(i),sqrt(1-zeta(i)^2));
  y=1 - 1/sqrt(1-zeta(i)^2)*exp(-zeta(i)*wn*t).*cos(wn*sqrt(1-zeta(i)^2)*t-phi);
  txt = ['\zeta = ',num2str(zeta(i))];
  hold on
  plot(t,y,'DisplayName',txt)
  xlabel('t(sec)')
  ylabel('y')
end
hold off
legend show

%%% Question 2

%% a)

f =
