function [s] = spectrum1DwithMelCepstrumTrial(sdata,infoaudio,channel_number)
[ROW,~] = size(sdata);

MAXSIZE = 2*infoaudio.SampleRate;

[flA,flP] = funSpectralData(sdata(:,channel_number),2*infoaudio.SampleRate);

%grid values on u and v axis as 2^grid value = [1 2 4 8 16 32 ....]
MAX_GRID_ID_ON_1D = floor(log2(infoaudio.SampleRate/2)) + 1;
fg = 2.^( 0:MAX_GRID_ID_ON_1D );


% weights size 400x400 matrix as (this can change)
% [ 1.0000    0.7071    0.5000    0.3536    0.2500    0.1768    0.1250    0.0884    0.0625 ]
wg = sqrt( (sort(fg,'descend')/sum(sort(fg,'descend')))/max(sort(fg,'descend')/sum(sort(fg,'descend'))) );

rc = (infoaudio.SampleRate + 1)/2;
%row and column distances separately on u and v axis respectively
for k = 1:MAXSIZE
        distanceU(k) = round(k-rc);
end


% gridDistanceIndex = [-sort(fg,'descend') fg] result as below to create grids based
% on distance matrices distanceU and distanceV; for example,  for a size of 400x400 matrix, it will be
% [-256  -128   -64   -32   -16    -8    -4    -2    -1     1     2     4     8    16    32    64   128   256]
gridDistance = [-sort(fg,'descend') fg];

fl = flA;
for gridRow = gridDistance
        
        %create grid region on U axis
        if gridRow == -1
            uArea = (distanceU >= gridRow) .* (distanceU < 0);
        elseif gridRow == 1
            uArea = (distanceU <= gridRow) .* (distanceU > 0);
        elseif gridRow < -1
            uArea = (distanceU >= gridRow) .* ( distanceU < (gridRow/2) );
        elseif gridRow > 1
            uArea = (distanceU <= gridRow) .* ( distanceU > (gridRow/2) );
        end
               
        z = logical(uArea);
        weight = wg( log2(abs(gridRow)) + 1 ) ;
        fl(z) =  weight * mean(fl(z));

end

flR = log( abs(flA - fl) + 1 );

% s = (abs(   ifft( exp(flR + 1i*flP))   ).^2 );
s = (abs(   ifft( exp(flR + 1i*flP), ROW )   ).^2 );