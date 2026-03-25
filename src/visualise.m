% Copyright (c) 2026 Jack Bennett <jdb@kosude.net>
% All Rights Reserved.
%
% See the LICENCE file for more information.

pts = genpoints("clusters", 100);

% plot analysed datapoints
scatter(pts(:,1), pts(:,2), "Marker", "+");
