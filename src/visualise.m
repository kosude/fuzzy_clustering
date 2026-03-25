% Copyright (c) 2026 Jack Bennett <jdb@kosude.net>
% All Rights Reserved.
%
% See the LICENCE file for more information.

pts = genpoints("clst", 100);

[centres] = algoFCM(pts, 5);

scatter(pts(:,1), pts(:,2), "Marker", "+");
hold on;
scatter(centres(:,1), centres(:,2), "filled", "Marker", "o");
hold off;
