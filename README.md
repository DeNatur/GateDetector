# GateDetector
AGH Drone Egineering attempt to make gate detector algorythm for Alpha Pilot Challenge


![alpha1](https://lh3.googleusercontent.com/ttOLIPe_r6py-_LE8_Q38MVe_kCAuBgHf15rjFtiQNfhnyn7kknfWenrc0pCBdtn28Wew-UskJZKGaRUxIYHbM7t-xFF1Xd5SArffJZH)

   Our algorithm is using previously trained weights file on more then 500 images provided by the organizers of the Alpha pilot challenge.
  We trained weights on all sort of images from every angle to provide the darknet trainer all possible options of the objects to detect.
  
  
  After detecting objects we take the corners with the highest confidence score and we use two opposing points to detect the midpoint 
  using Midpoint Formula. YOLO learns general representation of object so corners are ideal to detect fast and accurate from many possible 
  views.
  
   ![alpha2](https://lh4.googleusercontent.com/NACCXK2Ii3atQKsjEDe9MQDVRaX8vG1LKJB4a31xmjsl4zmWEG3yH0csFb77_-o0hy-XhWAHHvv19wShPRzts0cD9naW9H4VysmNOAoX)
  
  We wanted our detector to be able to detect the gate even when there are only two corners visible. So we came up with a 
  script which by using the only two corners visible and predictions where two others might be detected from the four possible points(top 
  left, top right, bottom right, bottom left). Then by bounding the whole gate and using predicted two points we can detect where the gate 
  is .
  
 ![alpha3](https://lh6.googleusercontent.com/btKN4qgCIbmbTBRNMiIlDQSQE2i7fPu47ENmM_25wzuUqUSLbPUA_cgQSm7oj_GA__S_UwpqnGT3oprqbmyoBE5_riBCzaZQiClG-IHMHLHsh1_E2rIzU1-ftLku-wF-kIPvgK45)
  
  
  If we detect three points we use mathematical formulas to classify which of the possible corners are our three detected. 
  Then by predicting which one we lack we use the corresponding x and y coordinates of the other three corners to evaluate the last, 
  lacking corner.

