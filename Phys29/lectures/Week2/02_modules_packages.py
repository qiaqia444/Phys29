{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Scalar Types in Core-Python"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Programming languages like Python have specific data types that reflect how information is stored in the computer memory.  We concentrate here on numbers, especially Integrers and Floats, and also Boolens (True of False). The table below summarizes the built-in simple scalar data types offered by Python, some of which we will discuss. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Python Scalar Types\n",
    "\n",
    "| Type        | Example        | Description                                                  |\n",
    "|-------------|----------------|--------------------------------------------------------------|\n",
    "| ``int``     | ``x = 1``      | integers (i.e., whole numbers)                               |\n",
    "| ``float``   | ``x = 1.0``    | floating-point numbers (i.e., real numbers)                  |\n",
    "| ``complex`` | ``x = 1 + 2j`` | Complex numbers (i.e., numbers with real and imaginary part) |\n",
    "| ``bool``    | ``x = True``   | Boolean: True/False values                                   |\n",
    "| ``str``     | ``x = 'abc'``  | String: characters or text                                   |\n",
    "| ``NoneType``| ``x = None``   | Special object indicating nulls                              |                   "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Integer Type"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Basic Integer operations"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5 2\n"
     ]
    }
   ],
   "source": [
    "a = 5  # assigning the integer value 5 to variable 'a'\n",
    "b = 2\n",
    "print(a,b)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Note that above we added comments to our code cell using the # symbol"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can verify that these variables have integer data types by using the type function native to python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "int"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(a)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The following operations are obvious, aren't they?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7 3\n",
      "10\n",
      "25\n",
      "2378064745833997089035291835260712838458865431811172691488433289557139138657603628438861986726706923349682264965985710377075584782188694692388947882175715519096675757218693363993962520205904428245134267078693818602685930613787403444349673750635551316739530524895408978060031103182470773666038096585996224572366020922922741813375977008950609768424189481012172621072842651947024496743122176907089835987862122732310713816419679412824662104973781214735145677660749637079556213075837285722443038754778346881579015918943327195917881149439724094933128669446556416470532227687870386234974128583815190410217053872782485805428030123508280668459404061483915456124322080471245927500999765814304079369997836412119328766896770025073773637881461886393763198491381533166250356427920171543091065325015639817188395887395256998812451647205410389780658706958486877635305492456193832833394713360657435410066143050999138740329543502360903770744096738684337640671289462134454882877648883255729913744107619012671861540790714616640142624237929502766607140809669974506851763768063425875275792176508417261388844451273907518292936167111873286406275996081702481440887180422148294186164804163727713622662064716750392223252809575011026769974375523428799048872277941771728393521054839358319000181760249272723266242288942313186347035691433675133873317412409327135279314709559425076477433653254749619019831030795005501074269414988195919783534048589478873525634740143523829122817094751801274630303237222595708990590193994111374446614605382522132568053594610847273612657388555713216334204672470663007665466715951810404851446568103499257336412444463214449080832087296272600344870025851740132664243647186578851593551620523607417121001554285508245430496057007049478498181585348797855244132931992745912758199610781955730830560516178514164952817821071919197567870992288020665195023661001515168378481710873875232163887727509509086330564846326035891739366440810242232213743571670477729583475445091682997961349353634876688026277882950389096803442365492207174237496871420450997430227805186939896202471224382610491433099418545319560788624138403215040331708488263608451676972326800356714308555498095226374153223101686278937792813415780922706806303797654418142235006817233403525647497473371778484863802932310418444344560353374733419050611562830811765300848267418452268679220537093842973746126123986374933330607916978275783183610388712087361311315748364653324096283458152449231322996047913194195832549480727793317312706785533968600359880607973194236959396729795223245499403820157924683203407395944305532033087698517288491650885240862709258607956082980298004826899041294620848740333907253498110062290510121396015239485301266435599317851076894072478145278501826556007768455292719741488428310590847439296376789570374925331618683765731335843069154983624067488401239819441815430296645234153782267807671398030272479146287370541629019685405335748389126630430926059059036906069296872669436019885693160711597880523526030134456898669975068245290874963831722995970995451081662157617127903626186488905656878054826729492009211872512534814759637626405059205624852253655207036316651611494277375865705672241082338163676392495155470566925198235296663206326710342063852710396626619293216407145026558498827339422165369492762658846770102887942817462425770073619226946360657630279347727268032466169801524152631703192139702865560804089767395772056135473398364693796901352162227561900879910394429237734787345643578488606299974853763517352495981449816581975846237812141745340372684095373341038116275144934949511817187625491372194658399549166227996588417645504894302258122316235692118804043605061213114386427823769378053950032466368595266921297666875709788692009375642443963768427691482346475403709300830163548363360947813655835665838589490137826494044193115229290924617089331150054931640625\n"
     ]
    }
   ],
   "source": [
    "print(a + b, a - b) # Integer addition and subtraction\n",
    "print(a * b)        # Integer multiplication\n",
    "print(a**b)         # 5 to the power of 2\n",
    "print(5**5460)      # 'arbitrarily accurate' integer arithmetic! "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What about the following. Is it what you would expect?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "x = a / b        # x is a new variable which is a/b, i.e. division\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Note that the type of x has changed though, it is no longer an integer but rather it has been promoted to a float, which is short for a floating point number. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "type(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Simultaneous assignment of values to different variables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# In contrast to many other languages, Python allows to simultaneously\n",
    "# assign values to severtal valriables:\n",
    "\n",
    "x = 5        # usual assignment\n",
    "y, z = 1, 2  # simultaneous assignemnt to two variables\n",
    "a, b, c, d = 6, 7, 8, 9 # works with arbitrarily many!\n",
    "\n",
    "print(a, b, c, d, x, y, z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Float Type"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "pi = 3.14159 # For full precision use numpy.pi\n",
    "d = .1       # equal to 0.1\n",
    "e = 1.2e2    # read: 1.2 times 10 to the power of 2\n",
    "\n",
    "print(pi + d, pi - d, d * e, pi / d)\n",
    "print(d + 3)  # in mixed calculations, integer values are 'promoted' to float"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Boolean Type\n",
    "Python has an *explicit* boolean type which can only take the values ```True``` and ```False```. It is used to test conditions in loops and conditional ```if``` statements and store information that can only be True or False. We could of course just use ```1``` to represent ```True``` and ```0``` to represent ```False```, however this would require more computer memory to store the information. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "f = False\n",
    "t = True\n",
    "type(f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(f or t)   # logical 'or' operator\n",
    "print(f and t)  # logical 'and' operator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = 1\n",
    "print(a == 1)   # test for equality\n",
    "print(a == 2)\n",
    "print(a < 5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "y = a >= 5\n",
    "print(y)\n",
    "type(y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If we assign a boolean statement to a new variable ```y```, y has boolean type, in another words the output of the boolean statement is boolean. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## String Type\n",
    "Strings in Python are created with single or double quotes:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "message = \"what do you like?\"\n",
    "response = 'spam'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Python has many extremely useful string functions and methods; here are a few of them:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# length of string\n",
    "len(response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Make upper-case. See also str.lower()\n",
    "response.upper()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Capitalize. See also str.title()\n",
    "message.capitalize()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# concatenation with +\n",
    "message + response"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# multiplication is multiple concatenation\n",
    "5 * response"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Access individual characters (zero-based indexing)\n",
    "message[0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We will explain more about indexing when we discuss Lists.  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Order of Operations"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "An **order of operations** is a standard order of precedence that different operations have in relationship to one another. Python utilizes the same order of operations that you learned in grade school. Powers are executed before multiplication and division, which are executed before addition and subtraction. Parentheses, (), can also be used in Python to supersede the standard order of operations. For example consider:\n",
    "\\begin{equation}\n",
    "\\frac{3\\times 4}{2^2 + 4/2}\n",
    "\\end{equation}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "x = (3*4)/(2**2 + 4/2)\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Operator precedence rules are summarised [here in Sec. 6.16](https://docs.python.org/3/reference/expressions.html).\n",
    "- They are generally valid, not only for integer operations, i.e. they apply to floats as well and outputs of functions!\n",
    "- **Advice**: Use parentheses to avoid any confusion and ambiguity! You should know the rules nevertheless to be able to read other peoples programs!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Aside: Scientific Notation"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We write numbers in scientific notation as, e.g., \n",
    "\\begin{equation}\n",
    "    c = 3 \\times 10^8~{\\rm m~s^{-1}}\n",
    "\\end{equation}\n",
    "(in SI units).  You may well need the value of $c$ for your calculation.  You could write\n",
    "\n",
    "```c = 3*10**8```\n",
    "\n",
    "However, you should not do this.  Instead, please write\n",
    "\n",
    "```c = 3e8```\n",
    "\n",
    "These are interpreted very differently by the computer.  The first one takes the integer 10, raises it to the 8$^{\\rm th}$ power, and then multiplies this by 3 and assigns the value to {\\tt c}.  The second one assigns the value of $3 \\times 10^8$ directly to the variable {\\tt c}.  The second way is faster, easier to read, and less vulnerable to bugs, as you will see or have seen in your first section.   For a quick look at one reason why you should write scientific notation as, e.g., ```3e8```, try the following:\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "However, you should not do this.  Instead, please write\n",
    "\n",
    "```c = 3e8```\n",
    "\n",
    "These are interpreted very differently by the computer.  The first one takes the integer 10, raises it to the 8$^{\\rm th}$ power, and then multiplies this by 3 and assigns the value to ```c```.  The second one assigns the value of $3 \\times 10^8$ directly to the variable ```c```.  The second way is faster, easier to read, and less vulnerable to bugs, as you will see or have seen in your first section.  \n",
    "For a quick look at one reason why you should write scientific notation as, e.g., ```3e8```, try the following:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "c = 3*10**8\n",
    "print(c)\n",
    "type(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "c = 3e8\n",
    "print(c)\n",
    "type(c)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "For a quick look at one reason why you should write scientific notation as, e.g., ```3e8```, try the following:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(1/3e8**2)\n",
    "print(1/3*10**8**2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Besides the issue above with the order of operations, there is a largest number and a smallest number (i.e. closest to zero) that a computer can represent because of details of how it stores numbers in memory (see below). Any number larger than about  $10^{308}$ or ```1e308``` will be stored as ```inf``` (and will generate a warning called overflow), while a number closer to zero than $10^{-308}$ or ```1e-308``` will be stored as ```0.0``` (and generate an underflow warning).  If you get one of these warnings, it's because some part of your program gave a result that was beyond one of these numbers. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can determine the largest and smallest numbers that can be represented by executing the following code:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys\n",
    "print(sys.float_info.max,sys.float_info.min)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "There exist clever tricks to circumvent these limitations, but there is no way to get around the fact that finite storage capcity necessarily results in finite precision for numerical calclulations involve floating point numbers, as we discuss in more detail next. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Aside: Floating-point precision\n",
    "One thing to be aware of with floating point arithmetic is that its precision is limited, which can cause equality tests to be unstable. For example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "0.1 + 0.2 == 0.3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Never ever compare float numbers to test for equality!!**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Why is this the case? It turns out that it is not a behavior unique to Python, but is due to the fixed-precision format of the binary floating-point storage used by most, if not all, scientific computing platforms.\n",
    "All programming languages using floating-point numbers store them in a fixed number of bits, and this leads some numbers to be represented only approximately.\n",
    "We can see this by printing the three values to high precision:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.1 = 0.10000000000000001\n",
      "0.2 = 0.20000000000000001\n",
      "0.3 = 0.29999999999999999\n"
     ]
    }
   ],
   "source": [
    "print(\"0.1 = {0:.17f}\".format(0.1))\n",
    "print(\"0.2 = {0:.17f}\".format(0.2))\n",
    "print(\"0.3 = {0:.17f}\".format(0.3))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We're accustomed to thinking of numbers in decimal (base-10) notation, so that each fraction must be expressed as a sum of powers of 10:\n",
    "$$\n",
    "1 /8 = 0.125 = 1\\cdot 10^{-1} + 2\\cdot 10^{-2} + 5\\cdot 10^{-3}\n",
    "$$\n",
    "In the familiar base-10 representation, we represent this in the familiar decimal expression: $0.125$.\n",
    "\n",
    "Computers usually store values in binary notation, so that each number is expressed as a sum of powers of 2:\n",
    "$$\n",
    "1/8 = 0\\cdot 2^{-1} + 0\\cdot 2^{-2} + 1\\cdot 2^{-3}\n",
    "$$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "0*(1/2) + 0*(1/2**2) + 1*(1/2**3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Notice that the coefficient in front of each term in base-2 is either 0 or 1, which is more appropriate to how information is stored on a computer, i.e. via electronic\n",
    "binary switches that can take on two possible values, i.e. on or off. In a base-2 representation, we can write this $0.001_2$, where the subscript 2 indicates binary notation.\n",
    "The value $0.125 = 0.001_2$ happens to be one number that both binary and decimal notation can represent in a finite number of digits.\n",
    "\n",
    "In the familiar base-10 representation of numbers, you are probably familiar with numbers that can't be expressed in a finite number of digits.\n",
    "For example, dividing $1$ by $3$ gives, in standard decimal notation:\n",
    "$$\n",
    "1 / 3 = 0.333333333\\cdots\n",
    "$$\n",
    "The 3s go on forever: that is, to truly represent this quotient, the number of required digits is infinite!\n",
    "\n",
    "Similarly, there are numbers for which binary representations require an infinite number of digits.\n",
    "For example:\n",
    "$$\n",
    "1 / 10 = 0.00011001100110011\\cdots_2\n",
    "$$\n",
    "If we consider only the first few terms we get:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.0999755859375"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "1/(2**4) + 1/(2**5) + 1/(2**8) + 1/(2**9) + 1/(2**12) + 1/(2**13)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Thus, just as decimal notation requires an infinite number of digits to perfectly represent $1/3$, binary notation requires an infinite number of digits to represent $1/10$.\n",
    "Python internally truncates these representations at 52 bits beyond the first nonzero bit on most systems. Here a bit is a binary switch, of which we have access to 64 at most on \n",
    "a 64-bit computer system. For a \"double-precision\" floating point number, one bit is used for the sign (positive or negative), 11 bits represent the integer exponent, and 52 bits\n",
    "represent the fraction. In other words a 64-bit floating point number is represented as\n",
    "\\begin{equation}\n",
    "(-1)^{\\rm sign}\\left(1 + \\sum_{i=1}^{52} b_{52-i}2^{-i}\\right)2^{e-1023}\n",
    "\\end{equation}"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "The bits are laid out in memory as follows:\n",
    "\n",
    "<img src=\"figures/float.png\" alt=\"floating point numbers\" width=\"800\">"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This rounding error for floating-point values is a necessary evil of working with floating-point numbers with a finite hardware representation. \n",
    "The best way to deal with it is to always keep in mind that floating-point arithmetic is approximate, and *never* rely on exact equality tests with floating-point values. If you need to compare floats, the Python `numpy`-module has a function for it:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "np.isclose(0.1 + 0.2, 0.3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Finally, we can now better see why ```1e-308``` and ```1e308``` are the smallest and largest numbers that can be represented by a 64-bit floating point number. Namely, as an 11bit integer, the exponent $e$ can range from 0 to 2047 ($2^11 = 2048$), which means that $e-1023$ in the equation above can run from $-1023$ to $+1024$. Hence, the smallest possible value is $2^{-1023} =$ ```1.1e-308``` and the largest possible value of $2^{1024} =$ ```1.8e308```."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Modules and Packages\n",
    "\n",
    "A good scientific calculator has all sorts of built-in functions like ```sin```, ```ln```, ```sqrt```.  These are also available to you in Python via\n",
    "**package** known as ```numpy```.   Modules and packages are libraries for Python code. You will use them constantly to use existing code. As a more experienced program you can write your own modules and packages to re-use your code. \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Modules \n",
    "\n",
    "A modules is a file with Python code with the .py suffix. It typically contains:\n",
    "- variable assignments\n",
    "- function definitions\n",
    "- classes/objects\n",
    "\n",
    "i.e. code that defines new functions or objects, but that do not immediately execute (although nothing prevents you from putting code that can execute in such a file).  In simple terms, we can consider a module to be a file that contains a set of variables, functions, or classes that you want to include in your application. \n",
    "\n",
    "The module name is the file name with the .py suffix. It can be **imported** into another Python program using the ```import``` statement.\n",
    "```python \n",
    "import module_name\n",
    "```\n",
    "\n",
    "where module_name.pay would be the python file for the module. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hbar = 1.054571818e-34\n"
     ]
    }
   ],
   "source": [
    "import constants\n",
    "two_pi = 2*constants.pi\n",
    "hbar = constants.h/two_pi\n",
    "print('hbar = {:.9e}'.format(hbar))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The contents of a module are accessed with the “dot” operator, e.g, constants.pi.\n",
    "\n",
    "Other ways to import: "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hbar = 1.054571818e-34\n",
      "hbar = 1.054571818e-34\n"
     ]
    }
   ],
   "source": [
    "# direct import\n",
    "from constants import h, pi\n",
    "hbar = h / (2*pi)\n",
    "print('hbar = {:.9e}'.format(hbar))\n",
    "\n",
    "# aliasing\n",
    "import constants as c\n",
    "hbar = c.h / (2*c.pi)\n",
    "print('hbar = {:.9e}'.format(hbar))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Packages\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "A Python package is a collectino of modules that are distributed together. \n",
    "- A package modularizes the modules. \n",
    "- Modules in a package are also accessed with the dot operator\n",
    "- Packages become important with working on larger projects. Many external Python libraries are distributed as packages. \n",
    "\n",
    "Like modules, packages need to be imported into your code using the command ```import```.  There are three very useful Python packages in particular which we will use in this course, and which in fact are the three most widely used in the sciences:  ```numpy```, ```scipy```, and ```matplotlib```.  For example, consider scipy which we will use in this course for several different applications: "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['LowLevelCallable',\n",
       " '__version__',\n",
       " 'cluster',\n",
       " 'constants',\n",
       " 'datasets',\n",
       " 'fft',\n",
       " 'fftpack',\n",
       " 'integrate',\n",
       " 'interpolate',\n",
       " 'io',\n",
       " 'linalg',\n",
       " 'misc',\n",
       " 'ndimage',\n",
       " 'odr',\n",
       " 'optimize',\n",
       " 'show_config',\n",
       " 'signal',\n",
       " 'sparse',\n",
       " 'spatial',\n",
       " 'special',\n",
       " 'stats',\n",
       " 'test']"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import scipy \n",
    "dir(scipy)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Note that scipy has a module known as constants, I can access it via the dot operator."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Scipy h = 6.626070150e-34\n",
      "My h= 6.626070150e-34\n"
     ]
    }
   ],
   "source": [
    "print('Scipy h = {:.9e}'.format(scipy.constants.Planck))\n",
    "print('My h= {:.9e}'.format(constants.h))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In this example, the constants.py module that I imported above not overwrite (or “shadow”) the scipy.constants module (or vice versa): they live in what are called different **namespaces**. Packages organize modules so that name collisions are avoided."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Below I provide an example that combines the use of the ``numpy```, ```scipy```, and ```matplotlib``` packages. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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t92G8+fP4+uvv8Z7770Hf39/AE0P1+Xk5GD48OGorKzEY489hg4dOmDdunW4+eab8f333+PWW2+td/4bb7wBuVyOf/7znygpKcFbb72F2bNn4+DBgwAAtVqNiRMnoqamBv/4xz8QHByMjIwMbNy4EcXFxfD29m7y/RuehcGDB2P58uXIycnBBx98gL179+L48ePw8fHBv/71L3Tv3h2rV682DsE29osRgFltsWfPHvz444945JFH4Onpif/85z+4/fbbkZaWhg4dOhjbaOjQocbi6oCAAGzevBkLFixAaWkpnnjiiWa/txqNpsFz4ubmBjc3tyZf8/nnn6O6uhoPPPAAVCoV/Pz88Mknn+Cxxx7DHXfcgccffxzV1dU4efIkDh48iFmzZrX4+3+t5ORk3HjjjXBycsLOnTubbNfGNPdcAMBnn32GBx98EMOHD8cTTzyBy5cv4+abb4afnx8iIiKavce+ffswcODABse3b9+OyZMno1OnTnjppZdQVVWFDz/8ECNGjMCxY8caFKLfeeed6Nq1K15//XUIggAAePHFF/Hqq69iypQpmDJlCo4dO4b4+Hio1ep6r23p50hj38PGnDp1CrW1tfV60gF9D1xMTAyOHz/e4DUDBw7E3r17m2s2MpdAZAGff/65AKDBfyqVSli7dm29c//66y8BgPDVV1/VO75ly5Z6x3/66ScBgHD48OEm7/v4448LXl5eQm1tbZPnvPLKK4K7u7tw/vz5esefe+45QaFQCGlpacZjAISlS5eafK8pKSmNvlcAws6dOwVBEITRo0cLo0ePbvDauXPnCh07dmxwrQ4dOgiFhYXG47/88osAQPjtt9+Mx2644QbB09NTuHLlSr1r6nQ64/9/++23BQBCSkpKg3t37NhRmDt3rvHfTzzxhABA+Ouvv4zHysrKhOjoaCEqKkrQarWCIAjCzp07BQBCz549hZqaGuO5H3zwgQBAOHXqlCAIgnD8+HEBgLBhw4amG68RarVaCAwMFPr06SNUVVUZj2/cuFEAILz44ovGY4bnzNQzYWCqLQAIzs7OwsWLF43HTpw4IQAQPvzwQ+OxBQsWCCEhIUJ+fn691999992Ct7e3UFlZaTKGjh07NvqcGJ6xpp4HLy8vITc3t961pk+fLvTu3bvV77kxc+fOFZRKpRASEiKEhoY2+Bm51vXPtLnPheH7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FbKyssQLup001zZpaWnCDTfcIPj5+QkqlUro0qWL8PTTTwslJSXiBt5O7rvvPqFjx46Cs7OzEBAQIIwbN07Ytm2b8ev29tzIBEEQ2jPxIiIiIrIVrBEiIiIih8VEiIiIiBwWEyEiIiJyWEyEiIiIyGExESIiIiKHxUSIiIiIHBYTISIiInJYTISIiIjIYTERIiIiIofFRIiIiIgcFhMhInIoeXl5CA4Oxuuvv248tm/fPjg7O9fbUZuIHAP3GiMih7Np0ybccsst2LdvH7p3746YmBhMnz4dK1asEDs0ImpnTISIyCE9+uij2L59OwYNGoRTp07h8OHDUKlUYodFRO2MiRAROaSqqir06dMHV69exdGjR9G3b1+xQyIiEbBGiIgc0qVLl5CZmQmdTofU1FSxwyEikbBHiIgcjlqtxpAhQxATE4Pu3bvj/fffx6lTpxAYGCh2aETUzpgIEZHDefrpp/H999/jxIkT8PDwwOjRo+Ht7Y2NGzeKHRoRtTMOjRGRQ9m1axfef/99fPHFF/Dy8oJcLscXX3yBv/76Cx9//LHY4RFRO2OPEBERETks9ggRERGRw2IiRERERA6LiRARERE5LCZCRERE5LCYCBEREZHDYiJEREREDouJEBERETksJkJERETksJgIERERkcNiIkREREQOi4kQEREROSwmQkREROSw/h+QXQRib4vbpgAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import numpy as np\n",
    "from scipy.special import jv   # jv is the function for the Bessel function of the first kind\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "x = np.linspace(0, 10*np.pi, 500) # Set up a linearly spaced domain between 0 and 30 with 500 points. \n",
    "y = jv(0, x)   # Compute the Bessel function of order 0 on this domain, i.e. y = J_0(x)\n",
    "# Make the plot\n",
    "plt.plot(x, y, label=r'$J_{}(x)$'.format(0))\n",
    "plt.title('Bessel Functions of the First Kind (order 0)')\n",
    "plt.xlabel('x')\n",
    "plt.ylabel('y')\n",
    "plt.grid(True)\n",
    "plt.legend()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Note that I have imported the ```numpy``` module and called it ```np```.  This just saves me typing out the full word ```numpy``` all the time, and indeed  ```np``` is a VERY common shorthand.  ```numpy``` has a lot of useful functions, including the trig functions and\n",
    "their inverses (e.g. ```np.arcsin()```), hyperbolic trig functions (e.g. ```np.sinh()```), the exponential function ```np.exp()```, logarithms (```np.log()``` is $\\ln$, the natural logarithm to base $e$ - if you want log base ten use ```np.log10()```), and the square root function ```np.sqrt()```.  It also has a number of useful mathematical constants, i.e. I used ```np.pi``` in the example above to access the constant $\\pi$. \n",
    "\n",
    "I also imported the ```scipy``` module so that I could access the Bessel functions in the ```scipy.special``` sub-module. In other words the ```scipy``` package is actually a collection of ```.py``` files arranged in a directory hierarchy, and so you can think of ```scipy.special``` as being the path to a file in that directory structure.  Finally, I used the statement ```import matplotlib.pyplot as plt``` to import the ```pyplot``` function (abbreviated as ```plt``` as is the standard) from the ```matplotlib.pyplot``` sub-module. \n",
    "\n",
    "Finally, take note of how I provided comments in my code via the ```#```, explaining the logic behind my reasoning. \n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
