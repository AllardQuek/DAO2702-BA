from PIL import Image
from io import BytesIO
import requests
import matplotlib.pyplot as plt

def print_players(player):
    
    player = player.reset_index(drop=True)
    num_player = len(player)
    rows = num_player // 3 + 1
    columns = min(num_player, 3)
    
    height = 4*rows if num_player > 1 else 3.8
    width = 3.5*columns if num_player > 1 else 3.2
    fig = plt.figure(figsize=(width, 4*rows))
    for i in range(num_player):
        ax = plt.subplot(rows, columns, i+1)
        r = requests.get(player.loc[i, 'Photo'])
        im = Image.open(BytesIO(r.content))
        ax.imshow(im, interpolation='nearest')
        ax.set_aspect(1)
        ax.axis('off')
        
        ax.set_title(r'$\bf{' + player.loc[i, "Name"] + r'}$', fontsize=13, loc='center')
        
        tx = 'Age:             {0}                                    \n'.format(player.loc[i, 'Age'])
        tx += 'Nationality:  {0}\n'.format(player.loc[i, 'Nationality'])
        club = str(player.loc[i, 'Club'])
        club = club[:20] + '...' if len(club) > 23 else club
        tx += 'Club:            {0}\n'.format(club)
        tx += 'Jersey No.:   {0}\n'.format(int(player.loc[i, 'Jersey Number']))
        tx += 'Position:      {0}\n'.format(player.loc[i, 'Best Position'])
        tx += 'Salary:         {0}\n'.format(player.loc[i, 'Wage'])
        tx += r'$\bf{Ratings: ~~~' + '{0}'.format(player.loc[i, 'Overall']) + r'}$'
        
        overall = player.loc[i, 'Overall']
        color = 'gold' if overall >= 75 else 'silver' if overall >= 65 else 'peru'
        attr = dict(boxstyle='round', facecolor=color, alpha=0.4)
        ax.text(-15, 110, tx, bbox=attr, fontsize=12)
        ax.set_ylim([110, 0])
    
    fig.tight_layout(w_pad=4.5, h_pad=2)    
    plt.show()
