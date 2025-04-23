function s_plane_responses()
    % Define poles and their colors
    poles = [1, -1, 4j, -4, 2+3j, -3+3j, -2+5j];
    colors = lines(numel(poles));
    
    % Create figure
    figure; hold on; axis equal;
    title('Pole Locations and Impulse Responses');
    xlabel('Real'); ylabel('Imaginary');
    xlim([-4.5, 3.5]); ylim([-0.5, 6]);
    grid on;

    t = linspace(0, 2.5, 500); % Time vector for step response

    linked = []; % To keep track of complex conjugates already linked

    for i = 1:numel(poles)
        p = poles(i);
        c = colors(i, :);

        % Mark pole
        plot(real(p), imag(p), 'x', 'Color', c, 'MarkerSize', 10, 'LineWidth', 2);

        sys = tf(1, [1 -p]); % so w can input 1-pole of system: H(s) = 1 / (s - p)

        % Step response
        [y, ~] = impulse(sys, t);

        % Place small response plot
        x_offset = 0.2;
        y_scale = 0.4;
        t_plot = real(p) + x_offset + (t / max(t)) * 0.7;
        y_plot = imag(p) + y * y_scale;
        plot(t_plot, y_plot, 'Color', c, 'LineWidth', 1);

        % If complex, draw dotted line between conjugates (once)
        if imag(p) ~= 0
            conj_index = find(poles == conj(p));
            if ~ismember(i, linked) && ~isempty(conj_index)
                plot([real(p), real(conj(p))], [imag(p), imag(conj(p))], ':', 'Color', [0.4, 0.4, 0.4]);
                linked = [linked i conj_index];
            end
        end
    end
end
