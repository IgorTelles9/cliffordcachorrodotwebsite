with open('divs_slider.txt', 'w') as writer:
    for i in range(13,23,1):
        writer.write('<div class="carousel-item">\n')
        writer.write('  <img src="media/slider/'+str(i)+'.jpeg" class="img-fluid">\n')       
        writer.write('</div>\n')