
    // function menuadju() {
    //     if (window.innerWidth > 500) {
    //       document.getElementById('nav4').style.display = 'none';
    //       document.getElementById('close').style.display='none'
    //       document.getElementById('menu').style.display='none'

    //     } else {
    //         document.getElementById('menu').style.display='block'

    //         document.getElementById('menuicon').addEventListener('click',function(){
    //             nav4=document.getElementById('nav4').style.display='block'
    //             document.getElementById('menu').style.display='none'
    //             document.getElementById('close').style.display='block'
    //             document.getElementById('closeicon').addEventListener('click',function(){
    //                 document.getElementById('close').style.display='none'
    //                 document.getElementById('nav4').style.display='none'
                    
            
    //                 document.getElementById('menu').style.display='block'
            
    //             })
            
            
    //             });
    //     }
    //   }
  
    //   // Initial check
    //   menuadju();
  
    //   // Attach resize event listener
    //   window.addEventListener('resize', menuadju);


    function menuadju() {
        if (window.innerWidth > 500) {
          document.getElementById('nav4').style.display = 'none';
          document.getElementById('close').style.display = 'none';
          document.getElementById('menu').style.display = 'none';
        } else {
          document.getElementById('menu').style.display = 'block';
        }
      }
  
      function setupEventListeners() {
        document.getElementById('menuicon').addEventListener('click', function() {
          document.getElementById('nav4').style.display = 'block';
          document.getElementById('menu').style.display = 'none';
          document.getElementById('close').style.display = 'block';
        });
  
        document.getElementById('closeicon').addEventListener('click', function() {
          document.getElementById('nav4').style.display = 'none';
          document.getElementById('menu').style.display = 'block';
          document.getElementById('close').style.display = 'none';
        });
      }
      menuadju();
      setupEventListeners();
  
      // Attach resize event listener
      window.addEventListener('resize', menuadju);



    // function menuadju() {
    //     if (window.innerWidth > 500) {
    //       document.getElementById('nav4').style.display = 'none';
    //       document.getElementById('close').style.display = 'none';
    //       document.getElementById('menu').style.display = 'none';
    //     } else {
    //       document.getElementById('menu').style.display = 'block';
    //     }
    //   }
  
    //   // Function to set up event listeners for menu interactions
    //   function setupEventListeners() {
    //     document.getElementById('menuicon').addEventListener('click', function() {
    //       document.getElementById('nav4').style.display = 'block';
    //       document.getElementById('menu').style.display = 'none';
    //       document.getElementById('close').style.display = 'block';
    //     });
  
    //     document.getElementById('closeicon').addEventListener('click', function() {
    //       document.getElementById('nav4').style.display = 'none';
    //       document.getElementById('menu').style.display = 'block';
    //       document.getElementById('close').style.display = 'none';
    //     });
    //   }
  
    //   // Debounce function to limit the rate of calling a function
    //   function debounce(func, wait) {
    //     let timeout;
    //     return function(...args) {
    //       clearTimeout(timeout);
    //       timeout = setTimeout(() => func.apply(this, args), wait);
    //     };
    //   }
  
    //   // Initial setup
    //   menuadju();
    //   setupEventListeners();
  
    //   // Attach resize event listener with debounce
    //   window.addEventListener('resize', debounce(menuadju, 300));

















        csl={'INDIA':['Kerala','Goa','Sikkim','Bihar','Assam'],
             'CHINA':['Hunan','Henan','Qinghai','Sichuan','Shanxi']
          
        }

        sdc={
          'Kerala':['Kollam','Kannur','Kochi','Kottayam','Palakkad'],
          'Goa':['Ponda','Mapusa','Margao','Panaji','Vasco da Gama'],
          'Sikkim':['Gangtok', 'Namchi', 'Gyalshing'],
          'Bihar':['Patna', 'Gaya', 'Bhagalpur'],
          'Assam':['Guwahati', 'Dibrugarh', 'Silchar'],
          'Hunan':['Changsha', 'Zhuzhou', 'Xiangtan'],
          'Henan':['Zhengzhou', 'Kaifeng', 'Luoyang'],
          'Qinghai':['Xining', 'Golmud', 'Delingha'],
          'Sichuan':['Chengdu', 'Mianyang', 'Dazhou'],
          'Shanxi':['Taiyuan', 'Datong', 'Yuncheng']
    
        }








    document.addEventListener('DOMContentLoaded', function() {
      country=document.getElementById('country')
      state=document.getElementById('state')
      city=document.getElementById('city')
     country.addEventListener('change', function() { 
      countryselected=this.value
      stateschoices=csl[countryselected]
      state.innerHTML = '<option value="">Select State</option>';
      for(i in stateschoices){
        stateselected=stateschoices[i]
    option=new Option(stateselected,stateselected)
    state.appendChild(option)
      }});

      state.addEventListener('change', function() { 
        stateselected=this.value
        citychoices=sdc[stateselected]
        city.innerHTML = '<option value="">Select City</option>';
        for(i in citychoices){
          cityselected=citychoices[i]
      optione=new Option(cityselected,cityselected)
      city.appendChild(optione)


    }})});
    













    document.addEventListener('DOMContentLoaded', function() {
      const time = document.getElementsByClassName('sec');

      function sec() {
        for(i=0;i<time.length;i++){
          time[i].style.display = 'none';
        }
      }

      setTimeout(sec, 3000);
  });
