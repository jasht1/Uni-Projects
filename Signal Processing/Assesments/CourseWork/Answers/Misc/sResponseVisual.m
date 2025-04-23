function s_plane_dynamics(poles, responseType)
    % Handle default arguments
    if nargin < 1 || isempty(poles)
        poles = [0.1 + 4j, -0.2 + 4j, -0.6 + 3j, -1 + 5j, -1 + 2j]; % good for frequency
        % poles = [1, -1, 4j, -4, 2+3j, -3+3j, -2+5j]; % good for impulse
    end
    if nargin < 2
        responseType = 'frequency';
    end

    % Set up figure
    figure; hold on;
    title(['S-Plane with ' responseType ' Responses']);
    xlabel('Real'); ylabel('Imaginary');
    xlim([-1.2, 0.4]); ylim([0, 5.25]);
    grid on;

    % Generate colors
    colors = lines(numel(poles));
    t = linspace(0, 2.5, 500); % Time vector for step response
    natural_freqs = abs(imag(poles)) + abs(real(poles));  % crude estimate
    w_min = min(natural_freqs)/10;
    w_max = max(natural_freqs)*1.5;
    w = logspace(log10(w_min), log10(w_max), 500);

    % Track complex pairs already linked
    linked = [];

    for i = 1:numel(poles)
        p = poles(i);
        c = colors(i, :);

        % Plot pole
        plot(real(p), imag(p), 'x', 'Color', c, 'MarkerSize', 10, 'LineWidth', 2);

        % Build transfer function
        if isreal(p)
            sys = tf(1, [1 -p]);
        else
            % Complex: use 2nd-order with both conjugate poles
            if real(p) < 0  % to keep stability
                pair = [1 -2*real(p) abs(p)^2];
                sys = tf(abs(p)^2, pair);
            else
                pair = [1 -2*real(p) abs(p)^2];
                sys = tf(abs(p)^2, pair); % unstable but plotted anyway
            end
        end

        % Determine plot
        x_offset = 0; scale = 0.4;

        switch lower(responseType)
            case 'step'
                [y, ~] = step(sys, t);
                t_plot = real(p) + x_offset + (t / max(t)) * 0.7;
                y_plot = imag(p) + y * scale;
                plot(t_plot, y_plot, 'Color', c, 'LineWidth', 1);

            case 'impulse'
                [y, ~] = impulse(sys, t);
                t_plot = real(p) + x_offset + (t / max(t)) * 0.7;
                y_plot = imag(p) + y * scale;
                plot(t_plot, y_plot, 'Color', c, 'LineWidth', 1);

            case 'frequency'
                [mag, ~] = bode(sys, w); % for mag
                % [~ , mag] = bode(sys, w); % for phase ignore bad vir name
                mag = squeeze(mag); % remove singleton dims
                w_norm = w / max(w);
                mag_db = max(20*log10(mag / max(mag)) / 2,-60);
                mag_shift = mag_db * scale/2;
                x_plot = real(p) + x_offset + w_norm * scale;
                y_plot = imag(p) + mag_shift;  % normalize to system max
                %fill([x_plot, fliplr(x_plot)],[imag(p) * ones(size(mag_shift)), fliplr(mag_shift+imag(p))], c, 'FaceAlpha', 0.2, 'EdgeColor', 'none'); % broken idk why
                plot(x_plot, y_plot, 'Color', c, 'LineWidth', 1);
        end

        % Connect complex conjugates
        if imag(p) ~= 0
            conj_index = find(poles == conj(p));
            if ~ismember(i, linked) && ~isempty(conj_index)
                plot([real(p), real(conj(p))], [imag(p), imag(conj(p))], ':', 'Color', [0.4, 0.4, 0.4]);
                linked = [linked i conj_index];
            end
        end
    end
end
