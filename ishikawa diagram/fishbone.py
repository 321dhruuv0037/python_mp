import numpy as np
#import pandas as pd
from pathlib import Path 
import matplotlib.pyplot as plt
import matplotlib

# =============================================================================
# AUX FUNCTIONS
# =============================================================================
def drawSpines(data:dict,ax:plt.Axes,parentSpine=None,alpha_ps:float=60.0,alpha_ss:float=0,recLevel=1,MAX_RECURSION_LEVEL:int=4,DEBUG=False): 
    #stop recursion if maximum level reached
    if recLevel > MAX_RECURSION_LEVEL:
        raise AttributeError('Max Recursion Level Reached')
    

    if isinstance(data, dict):
        # switch to correct angle depending on recursion level
        if recLevel % 2 != 0:
            alpha = alpha_ps
        else:
            alpha = alpha_ss
  
        if isinstance(parentSpine,matplotlib.lines.Line2D):
            #calculate parent data
            ([xpb,xpe],[ypb,ype]) = parentSpine.get_data()
        elif isinstance(parentSpine, matplotlib.text.Annotation):
            xpb,ypb = parentSpine.xy
            xpe,ype = parentSpine._x, parentSpine._y#parentSpine._arrow_relpos
        else:
            raise AttributeError('Wrong Spine Graphical Element')
            
        plen = np.sqrt((xpe-xpb)**2+(ype-ypb)**2)
        palpha = np.degrees(np.arctan2(ype-ypb,xpe-xpb))  
    
    
        # calculate spacing
        pairs = len(list(data.keys())) // 2 + len(list(data.keys())) % 2 +1 #calculate couple pairs, at least 1 pair to start at middle branch
        spacing = (plen) / pairs
        
        spine_count=0
        s=spacing
        #draw spine  
        for k in data.keys():
            # calculate arrow position in the graph
            if recLevel==1:# and spine_count <= 1: #fix first 2 spines spacing
                x_end = xpe-(s/1.5)*np.cos(np.radians(palpha))#0.9*xpe
                y_end = ype-s*np.sin(np.radians(palpha))
                
                x_start = x_end -s*np.cos(np.radians(alpha))
                y_start = y_end -s*np.sin(np.radians(alpha))
            else:
                x_end = xpe-s*np.cos(np.radians(palpha))
                y_end = ype-s*np.sin(np.radians(palpha))
                
                x_start = x_end -s*np.cos(np.radians(alpha))
                y_start = y_end -s*np.sin(np.radians(alpha))
            if DEBUG == True:
                print(f'k: {k}, x_start: {x_start}, y_start: {y_start}, x_end: {x_end}, y_end: {y_end}, alpha: {alpha} \n recLevel: {recLevel}, s:{s}, plen:{plen}, palpha:{palpha}')
            
            
            # draw arrow arc
            if recLevel==1:
                props = dict(boxstyle='round', facecolor='lightsteelblue', alpha=1.0)
                spine = ax.annotate(str.upper(k), xy=(x_end, y_end), xytext=(x_start, y_start),arrowprops=dict(arrowstyle="->",facecolor='black'),bbox=props,weight='bold')
            else:
                props = dict(boxstyle='round', facecolor='lavender', alpha=1.0)
                spine = ax.annotate(k, xy=(x_end, y_end), xytext=(x_start, y_start),arrowprops=dict(arrowstyle="->",facecolor='black'),bbox=props)
            # Call recursion to draw subspines
            drawSpines(data=data[k],ax=ax,parentSpine=spine,recLevel=recLevel+1)
    
            # next spine settings - same level
            alpha *= -1
            spine_count += 1
            if  spine_count %2 ==0:
                s= s+spacing 
    return None

def ishikawaplot(data,figSize=(20,10),left_margin:float=0.05,right_margin:float=0.05, alpha_ps:float=60.0,alpha_ss= 0.0,pd_width:int=0.1) -> plt.figure:  
    
    fig = plt.figure(figsize=figSize)
    ax  = fig.gca()
    ax.set_xlim(0,1.0)
    ax.set_ylim(0,1.0)
    
    ax.axis('off')
    #hide x-axis
    #ax.get_xaxis().set_visible(False)
    #hide y-axis
    #ax.get_yaxis().set_visible(False)
    
    #draw main spine
    mainSpine = ax.axhline(y=0.5,xmin=left_margin,xmax=1-right_margin-pd_width)
    #draw fish head
    props = dict(boxstyle='round', facecolor='wheat', alpha=1.0)
    ax.text((1-right_margin-pd_width), 0.5, str.upper(list(data.keys())[0]), fontsize=12,weight='bold',verticalalignment='center',horizontalalignment='left', bbox=props)
    #draw fish tail
    x = (0.0,0.0,left_margin)
    y = (0.5-left_margin,0.5+left_margin,0.5)
    ax.fill(x,y) #"b"
    
    #draw spines with recursion
    drawSpines(data=data[list(data.keys())[0]],ax=ax,parentSpine=mainSpine,alpha_ps = alpha_ps, alpha_ss = alpha_ss)
    
    plt.tight_layout()
    
    
    return fig

# =============================================================================
# Rooting
# =============================================================================
current_dir = Path(__file__).parent
output_path = current_dir / "Ishikawa.jpeg"


# =============================================================================
# USER DATA
# =============================================================================
data = {'Low Results in Sem I': {'Low Percentile Admission': {'Low Minority Cutoffs':'Change in admission criterion'},
                    'Preparation Time': {'Less Time for preparation ': {'Irregularities in starting the semester':'','Late admissions':''}
                               },
                    'Distractions':     {'College Fests': {'Social Assignments':'','Travelling Time':''}
                               },
                    'Incomplete Syllabus':  {'Lack of Coverage of Syllabus': {'Poor Teaching':''}
                              }
                    
                   }
       }


# =============================================================================
# MAIN CALL
# =============================================================================
if __name__ == '__main__':
    
    fig = ishikawaplot(data,figSize=(20,10))
    
    fig.show()
    
    fig.savefig(output_path, 
                     #dpi=800, 
                     format=None, 
                     #metadata=None,
                     bbox_inches=None, 
                     pad_inches=0.0,
                     facecolor='auto', 
                     edgecolor='auto',
                     orientation='landscape',
                     transparent=False,
                     backend=None)