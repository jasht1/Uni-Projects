num = [0.0675, 0.1350, 0.0675]; % Y(z)
den = [1, -1.2765, 0.4129]; % X(z)

impulse = impz(num, den, N); % this is 10 marks?

% Plotting
figure;
stem(0:N-1, impulse, 'filled');
title('Difference Equation Impulse Response');
xlabel('n (samples)');
ylabel('Amplitude');
grid on;
