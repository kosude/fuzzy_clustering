% Copyright (c) 2026 Jack Bennett <jdb@kosude.net>
% All Rights Reserved.
%
% See the LICENCE file for more information.

function [c, u, D] = algoFCM(x, N, m, minImpr, maxItr)
    % ALGOFCM - Fuzzy C-Means (FCM) clustering algorithm implementation.
    %
    % Input arguments:
    %  - x (doubles) -
    %     2-column, M-row array of point coordinates, for M points.
    %     Column 1 contains X values and column 2 contains Y values.
    %
    %  - N (uint32) -
    %     Amount of clusters in the data.
    %
    %  - m (double) -
    %     Fuzzy partition matrix exponent - controls degree of fuzzy overlap,
    %     i.e. number of datapoints that have significant membership in more
    %     than one cluster (so 'fuzziness' of boundaries between clusters).
    %
    %  - minImpr (double) -
    %     Optional. Default value: 1e-5
    %     Once the algorithm converges by less than this value, it will end.
    %
    %  - maxItr (uint32) -
    %     Optional. Default value: 100
    %     Maximum number of algorithm iterations allowed.
    %
    % Return values:
    %  - c (doubles) -
    %     2-column, N-row array containing cluster centre points.
    %
    %  - u (doubles) -
    %     N-column, M-row array containing the degree of membership from each
    %     of the N clusters for each of the M datapoints.
    %
    %  - D (doubles) -
    %     N-column, M-row array containing the distance of each of the M
    %     datapoints from each of the N clusters.

    arguments
        x (:, 2) double
        N (1, 1) uint32
        m (1, 1) double { mustBeGreaterThan(m, 1) }
        minImpr (1, 1) double = 1e-5
        maxItr (1, 1) uint32 = 100
    end

    M = size(x, 1); % number of datapoints
    % range of x array on each dimension
    xrangeX = max(x(:,1)) - min(x(:,1));
    xrangeY = max(x(:,2)) - min(x(:,2));

    % preallocate output arrays
    c = zeros(N, 2);
    u = zeros(M, N);
    D = zeros(M, N);

    % initially set cluster centres to random values
    % rand is in [0,1] - convert to [-0.5,0.5], then scale to fit the pts range
    c(:,1) = (rand(N, 1) - 0.5) .* (xrangeX * 2);
    c(:,2) = (rand(N, 1) - 0.5) .* (xrangeY * 2);

    % randomly initialise membership values for each point
    for xR = 1:M
        % N random doubles that add to one
        rnorm = rand(1, N);
        rnorm = rnorm / sum(rnorm);
        u(xR,:) = rnorm;
    end

    % repeated algorithm
    itrN = 1;
    while itrN <= maxItr
        % calculate each cluster centre
        for i = 1:N
            for j = 1:M
                c(i,:) = sum((u(j,i)^m) * x(j,:)) / sum((u(j,i)^m));
            end
        end

        % compute Euclidean distance from each point to each cluster centre.
        for i = 1:N
            for j = 1:M
                D(i,j) = sqrt((x(j,:) - c(i,:))' * (x(j,:) - c(i,:)));%//FIXME
            end
        end

        % see https://uk.mathworks.com/help/fuzzy/fuzzy-clustering.html

        itrN = itrN + 1;
    end
end
