% pole_dynamics_visual - Plot s or z poles with embedded
% step, impulse, or frequency responses beside each pole.
% Usage: pole_dynamics_visual(domain, responseType)
%   domain: one of ['s','z']
%   responseType: one of ['step','impulse', 'frequency']
%   e.g.
%     pole_dynamics_visual('z','frequency');

function pole_dynamics_visual(domain, responseType)

    if nargin < 1 || (~strcmp(domain,'s') && ~strcmp(domain,'z'))
        error("First argument must be 's' or 'z'.");
    end
    if nargin < 2 || isempty(responseType)
        responseType = 'frequency';
    end
    domain = lower(domain);
    responseType = lower(responseType);

    %% layout settings

    switch domain
      case 's'
        switch responseType
          case 'step'
            poles = [-1, -3, -5+2j, -5-2j];
            scale = 0.3; x_shift = 0.2; y_shift = 0;
            x_wspace = 0.5; y_wspace =0.5;
          case 'impulse'
            poles = [1, -1, 4j, -4, 2+3j, -3+3j, -2+5j];
            scale = 0.3; x_shift = 0; y_shift = 0;
            x_wspace = 0.5; y_wspace =0.5;
          otherwise  % frequency
            poles = [-0.2+4j, -0.6+3j, -1+5j, -1+2j];
            % poles = [0.9*exp(1j*pi/4), 0.9*exp(-1j*pi/4), ...
            %     0.6*exp(1j*pi/2), 0.6*exp(-1j*pi/2), 0.8];
            scale = 0.6; x_shift = 0.25; y_shift = 0;
            x_wspace = 0.5; y_wspace =0.5;
        end
      case 'z'
        switch responseType
          case 'step'
            poles = [0.5, 0.7, 0.6*exp(1j*pi/3), 0.6*exp(-1j*pi/3)];
            scale = 0.3; x_shift = 0.1; y_shift = 0.1;
            x_wspace = 0.5; y_wspace =0.5;
          case 'impulse'
            % poles = [0.8, 0.75*exp(1j*pi/4), 0.75*exp(-1j*pi/4)];
            scale = 0.35; x_shift = 0.15; y_shift = 0.1;
            x_wspace = 0.5; y_wspace =0.5;
          otherwise  % frequency
            poles = [0.9*exp(1j*pi/4), 0.9*exp(-1j*pi/4), ...
                     0.6*exp(1j*pi/2), 0.6*exp(-1j*pi/2), 0.8];
            scale = 0.4; x_shift = 0.1; y_shift = 0.05;
            x_wspace = 0.2; y_wspace =0.2;
        end
    end

    %% Figure setup

    reals = real(poles);
    imags = imag(poles);
    xlims = [min(reals)-x_wspace, max(reals)+x_wspace*2];
    ylims = [min(imags)-y_wspace, max(imags)+y_wspace];

    figure; hold on; axis equal;
    title(sprintf('%s-Plane with %s Responses', upper(domain), responseType));
    xlabel('Real'); ylabel('Imaginary');
    xlim(xlims); ylim(ylims);
    grid on;
    if strcmp(domain,'z')
        theta = linspace(0,2*pi,500);
        plot(cos(theta), sin(theta), 'k--','LineWidth',1.2);
    end

    %% Time/frequency axes
    t = linspace(0,2.5,500);
    n = 0:50;
    if strcmp(domain,'s')
        nf = abs(imag(poles)) + abs(real(poles));
        w_min = min(nf)/10;  w_max = max(nf)*1.5;
        w = logspace(log10(w_min), log10(w_max), 500);
    else
        w = linspace(0, pi, 256);
    end

    colors = lines(numel(poles));
    linked = [];

    %% Loop through poles
    for i = 1:numel(poles)
        p = poles(i);
        c = colors(i,:);
        plot(real(p), imag(p), 'x','Color',c,'MarkerSize',10,'LineWidth',2);

        % Build transfer function
        if isreal(p)
            if strcmp(domain,'s')
                sys = tf(1, [1, -p]);
            else
                sys = tf(1, [1, -p], -1);
            end
        else
            coeffs = [1, -2*real(p), abs(p)^2];
            if strcmp(domain,'s')
                sys = tf(abs(p)^2, coeffs);
            else
                sys = tf(abs(p)^2, coeffs, -1);
            end
        end

        %% Compute response
        switch responseType
          case 'step'
            if strcmp(domain,'s')
              [y, tt] = step(sys, t);
            else
              [y, tt] = step(sys, n);
            end
            y_row = y(:).';  % ensure row
            x_norm = (tt - tt(1)) / (tt(end)-tt(1));
            x_row = x_norm * scale + x_shift;
            x_plot = real(p) + x_row;
            y_plot = imag(p) + y_row * scale + y_shift;
            plot(x_plot, y_plot, 'Color',c,'LineWidth',1);

          case 'impulse'
            if strcmp(domain,'s')
              [y, tt] = impulse(sys, t);
            else
              y = impz(sys.num{1}, sys.den{1}, length(n)); % Use impz for discrete impulse
              tt = n;
            end
            y_row = y(:).';
            x_norm = (tt - tt(1)) / (tt(end)-tt(1));
            x_plot = real(p) + x_norm * scale + x_shift;
            y_plot = imag(p) + y_row * scale + y_shift;
            plot(x_plot, y_plot, 'Color',c,'LineWidth',1);

          case 'frequency'
            if strcmp(domain,'s')
              [mag, ~] = bode(sys, w);
              mag = squeeze(mag);
            else
              [h, w_out] = freqz(sys.num{1}, sys.den{1}, w);
              mag = abs(h);
              w = w_out;
            end
            mag_row = mag(:).' / max(mag(:));
            mag_db = 20*log10(mag_row);
            mag_db = max(mag_db, -60);
            y_row = mag_db * (scale/40);
            x_row = (w / max(w)) * scale + x_shift;
            x_plot = real(p) + x_row;
            y_plot = imag(p) + y_row + y_shift;

            % fancy shading
            baseline = imag(p) * ones(1, numel(x_plot));
            fill( [x_plot, fliplr(x_plot)], ...
                  [baseline, fliplr(y_plot)], ...
                  c, 'FaceAlpha',0.2, 'EdgeColor','none');
            plot(x_plot, y_plot, 'Color',c,'LineWidth',1);
        end

        %% Link poles
        if imag(p) ~= 0
            idx = find(abs(poles - conj(p)) < 1e-6);
            if ~ismember(i, linked) && ~isempty(idx)
                plot([real(p), real(conj(p))], [imag(p), imag(conj(p))], ...
                     ':','Color',[0.5,0.5,0.5]);
                linked = [linked, i, idx];
            end
        end
    end
end
