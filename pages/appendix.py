from build import sec, ask, src, box, table

P = 'ap'

intro = """
<p>This appendix is where the course goes next, and none of it is on the midterm.</p>
"""

s1 = sec('s1', 'A.1', 'Many trials', """
<p>One throw of a fair die gives a whole number from 1 to 6, and the six values are equally likely. The average of all six is 3.5, a value the die itself can never show.</p>
<p>Now throw the die several times and take the average of those throws. Do that again and again, and look at how far apart the highest and lowest averages are. The table was started in class with the first row and left for the simulator to finish. Below is one run of the simulator, a thousand averages at each setting.</p>
""" + table(['Throws in each average', 'Lowest average', 'Highest average', 'Difference'], [
    ['1', '1.00', '6.00', '5.00'],
    ['10', '1.90', '5.40', '3.50'],
    ['100', '2.91', '4.02', '1.11'],
    ['1,000', '3.33', '3.65', '0.32'],
], caption='One run of the simulator below. Because each row is the extreme of a thousand averages, your own run will differ, and the wider the setting the more it will differ.') + """
<p>Two things change together as the number of throws goes up. The averages lie closer to 3.5, so the difference between the highest and the lowest falls from 5.00 to 0.32. At the same time the averages themselves get finer. With ten throws an average is a multiple of one tenth, with a hundred throws a multiple of one hundredth, so the possible values are closer and closer together.</p>
<p>That second change is the same idea as 2.6, seen from the other side. A single throw is recorded on a coarse scale with six values on it. Averaging many throws of the same coarse thing produces a quantity that behaves as though it were continuous. Recording decides how fine a single value is, and averaging decides how fine a summary of many values is.</p>
<p>The class ended on what that means away from dice. Over a short run a person can be lucky or unlucky, and the luck is most of what you see. Over many trials the good and the bad luck cancel, and what is left is the thing you were trying to measure. Reading one quarter, one cohort or one trainer's year is reading a short run.</p>
""" + ask('If I repeated this whole exercise tomorrow, how different would my answer be?')
+ src('the die-throw table worked in class, and the discussion of what happens when many trials are averaged.'))

sim = """
<section id="sim">
<h2><span class="n">Simulator</span>Run it yourself</h2>
<p>Pick how many throws go into each average and how many averages to take, then run it. Nothing is sent anywhere; the throws happen in this page.</p>
<div class="sim">
  <div class="sim-row">
    <label for="simN">Throws in each average</label>
    <select id="simN">
      <option value="1">1</option>
      <option value="10" selected>10</option>
      <option value="100">100</option>
      <option value="1000">1,000</option>
    </select>
    <label for="simR">How many averages</label>
    <select id="simR">
      <option value="100">100</option>
      <option value="1000" selected>1,000</option>
      <option value="5000">5,000</option>
    </select>
    <button class="btn" id="simGo" type="button">Run</button>
  </div>
  <div class="sim-out" id="simOut" aria-live="polite"></div>
  <div class="sim-chart" id="simChart"></div>
  <p class="sim-note" id="simNote"></p>
</div>
<script>
(function(){
  var go=document.getElementById('simGo');
  if(!go)return;
  function run(){
    var n=+document.getElementById('simN').value, r=+document.getElementById('simR').value;
    var means=new Array(r), lo=Infinity, hi=-Infinity, sum=0;
    for(var i=0;i<r;i++){
      var t=0;
      for(var j=0;j<n;j++) t+=1+Math.floor(Math.random()*6);
      var m=t/n; means[i]=m; sum+=m;
      if(m<lo)lo=m; if(m>hi)hi=m;
    }
    var mean=sum/r;
    document.getElementById('simOut').innerHTML=
      '<span><b>'+lo.toFixed(2)+'</b>lowest average</span>'+
      '<span><b>'+hi.toFixed(2)+'</b>highest average</span>'+
      '<span><b>'+(hi-lo).toFixed(2)+'</b>difference</span>'+
      '<span><b>'+mean.toFixed(3)+'</b>average of them all</span>';
    var B=24, w=(6-1)/B, counts=new Array(B).fill(0), max=0;
    for(i=0;i<r;i++){
      var b=Math.floor((means[i]-1)/w); if(b<0)b=0; if(b>=B)b=B-1;
      counts[b]++; if(counts[b]>max)max=counts[b];
    }
    var bars='';
    for(i=0;i<B;i++){
      var h=max?Math.round(counts[i]/max*100):0;
      var from=(1+i*w).toFixed(2), to=(1+(i+1)*w).toFixed(2);
      bars+='<i style="height:'+h+'%" title="'+from+' to '+to+': '+counts[i]+'"></i>';
    }
    document.getElementById('simChart').innerHTML=
      '<div class="bars">'+bars+'</div><div class="axis"><span>1</span><span>3.5</span><span>6</span></div>';
    document.getElementById('simNote').textContent=
      'With '+n.toLocaleString('en-GB')+' throw'+(n===1?'':'s')+' in each average, an average can only be a multiple of '+
      (1/n).toFixed(n===1?0:(n===10?1:(n===100?2:3)))+', so the possible values are that far apart.';
  }
  go.addEventListener('click',run);
  run();
})();
</script>
</section>
"""

PAGE = {
    'file': 'appendix.html', 'nav': 'appendix',
    'title': 'Appendix. Many trials', 'sub': 'Appendix',
    'dek': 'Where the course goes next. None of this is on the midterm.',
    'toc': [('s1', 'A.1 Many trials'), ('sim', 'Run it yourself')],
    'body': intro + s1 + sim,
    'prev': ('closing.html', 'Closing'),
    'next': ('practice.html', 'Practice set'),
}
