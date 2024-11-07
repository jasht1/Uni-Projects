I'm having some trouble understanding the output of this code:
% definitions
f = @(x, y) (2 * x * y^2 + 4) / (2 * (3 - y * x^2));% the ODE function
tspan = [-1, 2];% Time interval
x0 = -1; y0 = 8;% Initial conditions
h_values = [0.1, 0.01, 0.001];% Step sizes

% Plotting
figure;
for h = h_values
    % Initialize arrays to store results
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
    %plot(x_values, y_values, 'o-', 'DisplayName', ['h = ' num2str(h)]);
    plot(x_values(x_values >= 0.2 & x_values <= 2), y_values(x_values >= 0.2 & x_values <= 2), 'o-', 'DisplayName', ['h = ' num2str(h)]);
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

% Adjust figure properties
set(gcf, 'Position', [100, 100, 800, 800]);

after the brief infinite spike at 0 explained by the denominator reaching 0 each graph goes negative and 

figure;

Es = (3+sqrt(-4.*x.^2.*(x-3)+9))/x.^2;

plot(x, Es, 'b', 'DisplayName', 'Exact Solution');


"

![[Pasted image 20231215232042.png]]