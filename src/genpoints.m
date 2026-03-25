% Copyright (c) 2026 Jack Bennett <jdb@kosude.net>
% All Rights Reserved.
%
% See the LICENCE file for more information.

function [pts] = genpoints(method, n)
    arguments
        method { validatestring(method, ["rand" "clst"]) }
        n (1, :)
    end

    pts = zeros(n, 2);

    switch method
        % generate random points
        case "rand"
            pts(:,1) = rand(1, 100);
            pts(:,2) = rand(1, 100);

        % generate random clustered data (courtesy of Nuno Fachada)
        case "clst"
            [data] = generateData(pi / 2, pi / 8, 5, 15, 15, 5, 1, 2, n);
            pts = data;

        % argument is validated so default case not needed
    end
end
