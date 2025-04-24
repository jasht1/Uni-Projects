function s_plane_responses()
    poles = [1, -1, 4j, -4, 2+3j, -3+3j, -2+5j];
    colors = lines(numel(poles));
    
    figure; hold on; axis equal;
    title('Pole Locations and Impulse Responses');
    xlabel('Real'); ylabel('Imaginary');
    xlim([-4.5, 3.5]); ylim([-0.5, 6]); % should make automatic
    grid on;

    t = linspace(0, 2.5, 500); % Tvec for step response

    for i = 1:numel(poles)
        p = poles(i);
        c = colors(i, :);

        % Mark pole
        plot(real(p), imag(p), 'x', 'Color', c, 'MarkerSize', 10, 'LineWidth', 2);

        sys = tf(1, [1 -p]); % so can input 1-pole of system: H(s) = 1 / (s - p)

        % Step response
        [y, ~] = impulse(sys, t);

        % Place small response plot
        x_offset = 0.2;
        y_scale = 0.4;
        t_plot = real(p) + x_offset + (t / max(t)) * 0.7;
        y_plot = imag(p) + y * y_scale;
        plot(t_plot, y_plot, 'Color', c, 'LineWidth', 1);
    end
end
