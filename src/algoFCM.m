% Copyright (c) 2026 Jack Bennett <jdb@kosude.net>
% All Rights Reserved.
%
% See the LICENCE file for more information.

function [centres] = algoFCM(pts, numC)
    arguments
        pts (:, 2)
        numC (1, 1)
    end

    centres = zeros(numC, 2);

    ptXRange = max(pts(:,1)) - min(pts(:,1));
    ptYRange = max(pts(:,2)) - min(pts(:,2));

    % initially set cluster centres to random values
    % rand is in [0,1] - convert to [-0.5,0.5], then scale to fit the pts range
    centres(:,1) = (rand(numC, 1) - 0.5) .* (ptXRange * 2);
    centres(:,2) = (rand(numC, 1) - 0.5) .* (ptYRange * 2);
end
