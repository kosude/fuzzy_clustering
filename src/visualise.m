% Copyright (c) 2026 Jack Bennett <jdb@kosude.net>
% All Rights Reserved.
%
% See the LICENCE file for more information.

pts = genpoints("clst", 100);

[c, u] = algoFCM(pts, 5, 2, maxItr=1);

scatter(pts(:,1), pts(:,2), "Marker", "+");
hold on;
scatter(c(:,1), c(:,2), "filled", "Marker", "o");
hold off;
