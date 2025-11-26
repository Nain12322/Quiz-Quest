import pygame
import sys
import random
import os

pygame.init()
pygame.mixer.init()


correct_sound = pygame.mixer.Sound("90s-game-ui-2-185095.mp3")  


SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
FPS = 60


screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_BLUE = (25, 35, 70)
LIGHT_BLUE = (100, 150, 255)
RED = (255, 50, 50)
GRAY = (100, 100, 100)
DARK_GRAY = (50, 50, 60)

GENRE_COLORS = {
    "HISTORICAL": (180, 120, 50),
    "SCIENCE": (80, 80, 200),
    "ENTERTAINMENT": (200, 50, 120),
    "GEOGRAPHY": (50, 150, 80),
    "SPORTS": (150, 50, 40),
    "LITERATURE": (120, 80, 180)
}

GENRE_BG = {
    "HISTORICAL": (120, 80, 40),
    "SCIENCE": (40, 50, 100),
    "ENTERTAINMENT": (100, 40, 80),
    "GEOGRAPHY": (30, 80, 50),
    "SPORTS": (80, 40, 30),
    "LITERATURE": (80, 50, 120)
}

GENRE_BG_IMAGES = {
    "HISTORICAL": "pixelated histroy background.jpg",
    "SCIENCE": "pixelated solar system.jpg",
    "ENTERTAINMENT": "pixelated movie theater.jpg",
    "GEOGRAPHY": "pixelated world map.jpg",
    "SPORTS": "pixelated sports background.jpg",
    "LITERATURE": "pixelated library.jpg"
}

QUIZ_DATA = {
    "HISTORICAL": [
        ("Who was the first President of the United States?", ["GEORGE WASHINGTON", "ABRAHAM LINCOLN", "THOMAS JEFFERSON", "JOHN ADAMS"], 0),
        ("In which year did World War II end?", ["1943", "1944", "1945", "1946"], 2),
        ("Who built the Great Wall of China?", ["QIN SHI HUANG", "GENGHIS KHAN", "KUBLAI KHAN", "MAO ZEDONG"], 0),
        ("Which empire was ruled by Julius Caesar?", ["GREEK EMPIRE", "ROMAN EMPIRE", "PERSIAN EMPIRE", "MONGOL EMPIRE"], 1),
        ("Who discovered America in 1492?", ["VASCO DA GAMA", "CHRISTOPHER COLUMBUS", "MARCO POLO", "FERDINAND MAGELLAN"], 1),
        ("Which revolution began in 1789?", ["AMERICAN REVOLUTION", "RUSSIAN REVOLUTION", "FRENCH REVOLUTION", "INDUSTRIAL REVOLUTION"], 2),
        ("Who was the first man on the moon?", ["BUZZ ALDRIN", "YURI GAGARIN", "NEIL ARMSTRONG", "JOHN GLENN"], 2),
        ("When did the Berlin Wall fall?", ["1987", "1988", "1989", "1990"], 2),
        ("Who was known as the Iron Lady?", ["INDIRA GANDHI", "MARGARET THATCHER", "GOLDA MEIR", "ANGELA MERKEL"], 1),
        ("When did World War I begin?", ["1912", "1913", "1914", "1915"], 2),
        ("Who was the first emperor of Rome?", ["JULIUS CAESAR", "AUGUSTUS", "NERO", "CALIGULA"], 1),
        ("Which year was the Declaration of Independence signed?", ["1774", "1775", "1776", "1777"], 2),
        ("Who led India to independence?", ["JAWAHARLAL NEHRU", "MAHATMA GANDHI", "SUBHAS CHANDRA BOSE", "BHAGAT SINGH"], 1),
        ("When did the Titanic sink?", ["1910", "1911", "1912", "1913"], 2),
        ("Who was the last Tsar of Russia?", ["NICHOLAS I", "ALEXANDER II", "ALEXANDER III", "NICHOLAS II"], 3),
        ("Which civilization built Machu Picchu?", ["AZTEC", "MAYA", "INCA", "OLMEC"], 2),
        ("When did Columbus discover America?", ["1490", "1491", "1492", "1493"], 2),
        ("Who wrote the Communist Manifesto?", ["LENIN", "STALIN", "KARL MARX", "MAO ZEDONG"], 2),
        ("When did the American Civil War end?", ["1863", "1864", "1865", "1866"], 2),
        ("Who was the first female Prime Minister of the UK?", ["THERESA MAY", "MARGARET THATCHER", "ELIZABETH II", "INDIRA GANDHI"], 1),
        ("Which empire did Alexander the Great rule?", ["ROMAN", "PERSIAN", "MACEDONIAN", "GREEK"], 2),
        ("When was the United Nations founded?", ["1943", "1944", "1945", "1946"], 2),
        ("Who discovered penicillin?", ["LOUIS PASTEUR", "ALEXANDER FLEMING", "MARIE CURIE", "JONAS SALK"], 1),
        ("When did the Soviet Union collapse?", ["1989", "1990", "1991", "1992"], 2),
        ("Who was the leader of Nazi Germany?", ["MUSSOLINI", "HITLER", "STALIN", "FRANCO"], 1),
        ("Which year was the Magna Carta signed?", ["1215", "1315", "1415", "1515"], 0),
        ("Who was the first female pharaoh?", ["CLEOPATRA", "NEFERTITI", "HATSHEPSUT", "NEFERTARI"], 2),
        ("When did the French Revolution end?", ["1797", "1798", "1799", "1800"], 2),
        ("Who painted the Sistine Chapel?", ["LEONARDO DA VINCI", "RAPHAEL", "MICHELANGELO", "DONATELLO"], 2),
        ("Which war was fought from 1950-1953?", ["VIETNAM WAR", "KOREAN WAR", "GULF WAR", "IRAQ WAR"], 1),
        ("Who was the first President of South Africa?", ["MANDELA", "MBEKI", "DE KLERK", "ZUMA"], 0),
        ("When did India gain independence?", ["1945", "1946", "1947", "1948"], 2),
        ("Who led the Bolshevik Revolution?", ["STALIN", "LENIN", "TROTSKY", "MARX"], 1),
        ("Which empire built the Colosseum?", ["GREEK", "ROMAN", "BYZANTINE", "OTTOMAN"], 1),
        ("When was the first nuclear bomb dropped?", ["1943", "1944", "1945", "1946"], 2),
        ("Who was Queen of England for 63 years?", ["ELIZABETH I", "VICTORIA", "ELIZABETH II", "MARY I"], 1),
        ("Which city was the capital of the Byzantine Empire?", ["ROME", "ATHENS", "CONSTANTINOPLE", "ALEXANDRIA"], 2),
        ("When did the Renaissance begin?", ["13TH CENTURY", "14TH CENTURY", "15TH CENTURY", "16TH CENTURY"], 1),
        ("Who discovered the tomb of Tutankhamun?", ["HOWARD CARTER", "JEAN-FRANCOIS CHAMPOLLION", "FLINDERS PETRIE", "ZAHI HAWASS"], 0),
        ("Which war ended with the Treaty of Versailles?", ["NAPOLEONIC WARS", "WORLD WAR I", "WORLD WAR II", "FRANCO-PRUSSIAN WAR"], 1),
        ("Who was the founder of the Mongol Empire?", ["KUBLAI KHAN", "GENGHIS KHAN", "TAMERLANE", "ATTILA"], 1),
        ("When did the Black Death occur?", ["1247-1251", "1347-1351", "1447-1451", "1547-1551"], 1),
        ("Who was the first woman to fly solo across the Atlantic?", ["BESSIE COLEMAN", "AMELIA EARHART", "JACQUELINE COCHRAN", "HARRIET QUIMBY"], 1),
        ("Which civilization invented paper?", ["EGYPTIAN", "CHINESE", "INDIAN", "MESOPOTAMIAN"], 1),
        ("When was the first modern Olympics held?", ["1892", "1894", "1896", "1898"], 2),
        ("Who was the leader of the USSR during WWII?", ["LENIN", "STALIN", "KHRUSHCHEV", "BREZHNEV"], 1),
        ("Which treaty ended World War I?", ["TREATY OF PARIS", "TREATY OF VERSAILLES", "TREATY OF VIENNA", "TREATY OF GHENT"], 1),
        ("Who invented the printing press?", ["JOHANN GUTENBERG", "WILLIAM CAXTON", "ALDUS MANUTIUS", "NICOLAS JENSON"], 0),
        ("When did the Industrial Revolution begin?", ["1650", "1700", "1760", "1800"], 2),
        ("Who was the longest reigning British monarch?", ["VICTORIA", "ELIZABETH I", "ELIZABETH II", "GEORGE III"], 2),
    ],
    "SCIENCE": [
        ("What is the chemical symbol for gold?", ["GO", "GD", "AU", "AG"], 2),
        ("How many planets are in our solar system?", ["7", "8", "9", "10"], 1),
        ("What is the speed of light?", ["300000 KM/S", "150000 KM/S", "450000 KM/S", "200000 KM/S"], 0),
        ("What is H2O?", ["OXYGEN", "HYDROGEN", "WATER", "HELIUM"], 2),
        ("Who developed the theory of relativity?", ["ISAAC NEWTON", "ALBERT EINSTEIN", "STEPHEN HAWKING", "GALILEO GALILEI"], 1),
        ("What is the largest organ in human body?", ["LIVER", "BRAIN", "HEART", "SKIN"], 3),
        ("What gas do plants absorb?", ["OXYGEN", "NITROGEN", "CARBON DIOXIDE", "HYDROGEN"], 2),
        ("How many bones are in the human body?", ["196", "206", "216", "226"], 1),
        ("What is the atomic number of carbon?", ["4", "6", "8", "12"], 1),
        ("What is the powerhouse of the cell?", ["NUCLEUS", "MITOCHONDRIA", "RIBOSOME", "CHLOROPLAST"], 1),
        ("What is the boiling point of water in Celsius?", ["90", "95", "100", "105"], 2),
        ("Who discovered gravity?", ["GALILEO", "NEWTON", "EINSTEIN", "ARISTOTLE"], 1),
        ("What is the chemical formula for salt?", ["NaCl", "KCl", "CaCl2", "MgCl2"], 0),
        ("How many chromosomes do humans have?", ["23", "44", "46", "48"], 2),
        ("What is the smallest unit of life?", ["ATOM", "MOLECULE", "CELL", "TISSUE"], 2),
        ("What planet is known as the Red Planet?", ["VENUS", "MARS", "JUPITER", "SATURN"], 1),
        ("What is the study of weather called?", ["GEOLOGY", "METEOROLOGY", "ASTRONOMY", "OCEANOGRAPHY"], 1),
        ("What is the hardest natural substance?", ["GOLD", "IRON", "DIAMOND", "PLATINUM"], 2),
        ("How many elements are in the periodic table?", ["108", "112", "116", "118"], 3),
        ("What is the center of an atom called?", ["ELECTRON", "PROTON", "NUCLEUS", "NEUTRON"], 2),
        ("What gas do humans exhale?", ["OXYGEN", "NITROGEN", "CARBON DIOXIDE", "HYDROGEN"], 2),
        ("What is the largest planet?", ["EARTH", "SATURN", "JUPITER", "NEPTUNE"], 2),
        ("What is the process plants use to make food?", ["RESPIRATION", "PHOTOSYNTHESIS", "DIGESTION", "FERMENTATION"], 1),
        ("What is the symbol for sodium?", ["S", "So", "Na", "N"], 2),
        ("How many hearts does an octopus have?", ["1", "2", "3", "4"], 2),
        ("What is the closest star to Earth?", ["PROXIMA CENTAURI", "THE SUN", "SIRIUS", "ALPHA CENTAURI"], 1),
        ("What is the most abundant gas in Earth's atmosphere?", ["OXYGEN", "CARBON DIOXIDE", "NITROGEN", "HYDROGEN"], 2),
        ("What is the pH of pure water?", ["5", "6", "7", "8"], 2),
        ("What is the speed of sound?", ["243 M/S", "343 M/S", "443 M/S", "543 M/S"], 1),
        ("Who invented the telephone?", ["EDISON", "BELL", "TESLA", "MARCONI"], 1),
        ("What is the largest bone in the human body?", ["HUMERUS", "TIBIA", "FEMUR", "FIBULA"], 2),
        ("What is the chemical symbol for iron?", ["I", "Ir", "Fe", "In"], 2),
        ("How many moons does Mars have?", ["1", "2", "3", "4"], 1),
        ("What is the study of fossils called?", ["ARCHAEOLOGY", "PALEONTOLOGY", "GEOLOGY", "ANTHROPOLOGY"], 1),
        ("What is the melting point of ice in Celsius?", ["-1", "0", "1", "2"], 1),
        ("What is the largest ocean mammal?", ["ORCA", "SPERM WHALE", "BLUE WHALE", "HUMPBACK WHALE"], 2),
        ("What is the chemical symbol for helium?", ["H", "He", "Hl", "Ho"], 1),
        ("How many teeth does an adult human have?", ["28", "30", "32", "34"], 2),
        ("What is the most abundant element in the universe?", ["OXYGEN", "CARBON", "HYDROGEN", "HELIUM"], 2),
        ("What is the normal human body temperature in Celsius?", ["35", "36", "37", "38"], 2),
        ("What is the smallest bone in the human body?", ["STAPES", "INCUS", "MALLEUS", "HYOID"], 0),
        ("What is the study of earthquakes called?", ["GEOLOGY", "SEISMOLOGY", "VOLCANOLOGY", "METEOROLOGY"], 1),
        ("How many chambers does the human heart have?", ["2", "3", "4", "5"], 2),
        ("What is the largest land animal?", ["RHINO", "HIPPO", "ELEPHANT", "GIRAFFE"], 2),
        ("What is the chemical symbol for silver?", ["S", "Si", "Ag", "Sr"], 2),
        ("What is the tallest type of grass?", ["WHEAT", "BAMBOO", "CORN", "SUGARCANE"], 1),
        ("What is the freezing point of water in Fahrenheit?", ["0", "16", "32", "48"], 2),
        ("What is the study of birds called?", ["ZOOLOGY", "ORNITHOLOGY", "ENTOMOLOGY", "ICHTHYOLOGY"], 1),
        ("How many legs does a spider have?", ["6", "8", "10", "12"], 1),
        ("What is the largest internal organ?", ["HEART", "LUNG", "LIVER", "STOMACH"], 2),
    ],
    "ENTERTAINMENT": [
        ("Who directed the movie 'Inception'?", ["STEVEN SPIELBERG", "CHRISTOPHER NOLAN", "JAMES CAMERON", "QUENTIN TARANTINO"], 1),
        ("Which movie won the Oscar for Best Picture in 2020?", ["JOKER", "1917", "PARASITE", "ONCE UPON A TIME"], 2),
        ("Who played Iron Man in Marvel movies?", ["CHRIS EVANS", "CHRIS HEMSWORTH", "ROBERT DOWNEY JR", "MARK RUFFALO"], 2),
        ("Which actor is known as King Khan?", ["AAMIR KHAN", "SALMAN KHAN", "SHAH RUKH KHAN", "SAIF ALI KHAN"], 2),
        ("Who composed the Titanic theme song?", ["HANS ZIMMER", "JAMES HORNER", "JOHN WILLIAMS", "ENNIO MORRICONE"], 1),
        ("Which TV series features dragons?", ["BREAKING BAD", "STRANGER THINGS", "GAME OF THRONES", "THE WALKING DEAD"], 2),
        ("Who directed '3 Idiots'?", ["KARAN JOHAR", "RAJKUMAR HIRANI", "SANJAY LEELA BHANSALI", "ANURAG KASHYAP"], 1),
        ("Which movie has the song 'My Heart Will Go On'?", ["THE NOTEBOOK", "TITANIC", "ROMEO AND JULIET", "PEARL HARBOR"], 1),
        ("Who played Jack Sparrow?", ["ORLANDO BLOOM", "JOHNNY DEPP", "GEOFFREY RUSH", "BILL NIGHY"], 1),
        ("Which movie won 11 Oscars?", ["AVATAR", "TITANIC", "LORD OF THE RINGS", "BEN-HUR"], 1),
        ("Who directed The Dark Knight?", ["ZACK SNYDER", "CHRISTOPHER NOLAN", "TIM BURTON", "JOEL SCHUMACHER"], 1),
        ("Which actress played Hermione in Harry Potter?", ["BONNIE WRIGHT", "EMMA WATSON", "EVANNA LYNCH", "HELENA BONHAM CARTER"], 1),
        ("Who sang 'Thriller'?", ["PRINCE", "MICHAEL JACKSON", "JAMES BROWN", "STEVIE WONDER"], 1),
        ("Which movie features the character Joker?", ["SPIDER-MAN", "BATMAN", "SUPERMAN", "IRON MAN"], 1),
        ("Who directed Jurassic Park?", ["JAMES CAMERON", "STEVEN SPIELBERG", "GEORGE LUCAS", "RIDLEY SCOTT"], 1),
        ("Which band sang 'Bohemian Rhapsody'?", ["THE BEATLES", "QUEEN", "LED ZEPPELIN", "PINK FLOYD"], 1),
        ("Who played Forrest Gump?", ["TOM CRUISE", "TOM HANKS", "BRAD PITT", "LEONARDO DICAPRIO"], 1),
        ("Which movie features the song 'Let It Go'?", ["TANGLED", "FROZEN", "MOANA", "BRAVE"], 1),
        ("Who directed Avatar?", ["PETER JACKSON", "JAMES CAMERON", "STEVEN SPIELBERG", "CHRISTOPHER NOLAN"], 1),
        ("Which actor played Wolverine?", ["HENRY CAVILL", "HUGH JACKMAN", "CHRIS HEMSWORTH", "CHRIS EVANS"], 1),
        ("Who sang 'Shape of You'?", ["JUSTIN BIEBER", "ED SHEERAN", "SHAWN MENDES", "HARRY STYLES"], 1),
        ("Which movie won Best Picture in 2024?", ["BARBIE", "OPPENHEIMER", "KILLERS OF THE FLOWER MOON", "POOR THINGS"], 1),
        ("Who played Batman in The Dark Knight?", ["BEN AFFLECK", "CHRISTIAN BALE", "MICHAEL KEATON", "GEORGE CLOONEY"], 1),
        ("Which TV show features Walter White?", ["THE WIRE", "BREAKING BAD", "BETTER CALL SAUL", "NARCOS"], 1),
        ("Who directed Pulp Fiction?", ["MARTIN SCORSESE", "QUENTIN TARANTINO", "COEN BROTHERS", "DAVID FINCHER"], 1),
        ("Which movie features the character Simba?", ["BAMBI", "THE LION KING", "JUNGLE BOOK", "TARZAN"], 1),
        ("Who sang 'Billie Jean'?", ["PRINCE", "MICHAEL JACKSON", "STEVIE WONDER", "MARVIN GAYE"], 1),
        ("Which actress won an Oscar for La La Land?", ["EMMA STONE", "EMMA WATSON", "JENNIFER LAWRENCE", "NATALIE PORTMAN"], 0),
        ("Who directed The Godfather?", ["MARTIN SCORSESE", "FRANCIS FORD COPPOLA", "BRIAN DE PALMA", "SERGIO LEONE"], 1),
        ("Which movie features Buzz Lightyear?", ["CARS", "TOY STORY", "FINDING NEMO", "MONSTERS INC"], 1),
        ("Who played Spider-Man in 2002?", ["ANDREW GARFIELD", "TOBEY MAGUIRE", "TOM HOLLAND", "MILES MORALES"], 1),
        ("Which band sang 'Hotel California'?", ["THE DOORS", "EAGLES", "FLEETWOOD MAC", "AMERICA"], 1),
        ("Who directed Schindler's List?", ["ROMAN POLANSKI", "STEVEN SPIELBERG", "RIDLEY SCOTT", "OLIVER STONE"], 1),
        ("Which movie features the character Elsa?", ["TANGLED", "FROZEN", "BRAVE", "MOANA"], 1),
        ("Who sang 'Rolling in the Deep'?", ["BEYONCE", "ADELE", "TAYLOR SWIFT", "RIHANNA"], 1),
        ("Which actor played Neo in The Matrix?", ["JOHNNY DEPP", "KEANU REEVES", "BRAD PITT", "TOM CRUISE"], 1),
        ("Who directed Interstellar?", ["DENIS VILLENEUVE", "CHRISTOPHER NOLAN", "RIDLEY SCOTT", "JAMES CAMERON"], 1),
        ("Which movie won Best Picture in 2023?", ["TOP GUN MAVERICK", "EVERYTHING EVERYWHERE", "THE FABELMANS", "TAR"], 1),
        ("Who played Captain America?", ["CHRIS HEMSWORTH", "CHRIS EVANS", "CHRIS PRATT", "CHRIS PINE"], 1),
        ("Which band sang 'Stairway to Heaven'?", ["THE BEATLES", "LED ZEPPELIN", "PINK FLOYD", "THE ROLLING STONES"], 1),
        ("Who directed Fight Club?", ["CHRISTOPHER NOLAN", "DAVID FINCHER", "DENIS VILLENEUVE", "DARREN ARONOFSKY"], 1),
        ("Which movie features Woody the cowboy?", ["CARS", "TOY STORY", "A BUG'S LIFE", "MONSTERS INC"], 1),
        ("Who sang 'Shake It Off'?", ["ARIANA GRANDE", "TAYLOR SWIFT", "KATY PERRY", "MILEY CYRUS"], 1),
        ("Which actress played Wonder Woman?", ["SCARLETT JOHANSSON", "GAL GADOT", "BRIE LARSON", "MARGOT ROBBIE"], 1),
        ("Who directed The Shawshank Redemption?", ["FRANK DARABONT", "ROB REINER", "CLINT EASTWOOD", "STEVEN SPIELBERG"], 0),
        ("Which movie features the character Shrek?", ["MADAGASCAR", "SHREK", "KUNG FU PANDA", "HOW TO TRAIN YOUR DRAGON"], 1),
        ("Who sang 'Someone Like You'?", ["BEYONCE", "ADELE", "ALICIA KEYS", "CHRISTINA AGUILERA"], 1),
        ("Which actor played Joker in 2019?", ["JARED LETO", "JOAQUIN PHOENIX", "HEATH LEDGER", "JACK NICHOLSON"], 1),
        ("Who directed E.T.?", ["GEORGE LUCAS", "STEVEN SPIELBERG", "ROBERT ZEMECKIS", "JAMES CAMERON"], 1),
        ("Which band sang 'Sweet Child O' Mine'?", ["AEROSMITH", "GUNS N' ROSES", "METALLICA", "AC/DC"], 1),
    ],
    "GEOGRAPHY": [
        ("What is the capital of France?", ["LONDON", "BERLIN", "PARIS", "ROME"], 2),
        ("Which is the largest ocean?", ["ATLANTIC", "INDIAN", "ARCTIC", "PACIFIC"], 3),
        ("How many continents are there?", ["5", "6", "7", "8"], 2),
        ("Which country has the most population?", ["INDIA", "CHINA", "USA", "INDONESIA"], 1),
        ("What is the longest river in the world?", ["AMAZON", "NILE", "YANGTZE", "MISSISSIPPI"], 1),
        ("Which is the smallest country?", ["MONACO", "VATICAN CITY", "SAN MARINO", "LIECHTENSTEIN"], 1),
        ("Mount Everest is located in which country?", ["INDIA", "CHINA", "NEPAL", "BHUTAN"], 2),
        ("Which desert is the largest?", ["GOBI", "SAHARA", "ARABIAN", "KALAHARI"], 1),
        ("What is the capital of Japan?", ["OSAKA", "KYOTO", "TOKYO", "HIROSHIMA"], 2),
        ("Which country has the most islands?", ["INDONESIA", "SWEDEN", "PHILIPPINES", "CANADA"], 1),
        ("What is the capital of Australia?", ["SYDNEY", "MELBOURNE", "CANBERRA", "BRISBANE"], 2),
        ("Which is the largest country by area?", ["CANADA", "RUSSIA", "CHINA", "USA"], 1),
        ("What is the capital of Brazil?", ["SAO PAULO", "RIO DE JANEIRO", "BRASILIA", "SALVADOR"], 2),
        ("Which is the deepest ocean?", ["ATLANTIC", "INDIAN", "ARCTIC", "PACIFIC"], 3),
        ("What is the capital of Egypt?", ["ALEXANDRIA", "CAIRO", "GIZA", "LUXOR"], 1),
        ("Which country has the longest coastline?", ["RUSSIA", "CANADA", "INDONESIA", "AUSTRALIA"], 1),
        ("What is the capital of Canada?", ["TORONTO", "MONTREAL", "OTTAWA", "VANCOUVER"], 2),
        ("Which is the highest waterfall?", ["NIAGARA", "VICTORIA", "ANGEL", "IGUAZU"], 2),
        ("What is the capital of Italy?", ["MILAN", "VENICE", "ROME", "FLORENCE"], 2),
        ("Which continent has no permanent residents?", ["AUSTRALIA", "ANTARCTICA", "ARCTIC", "SOUTH AMERICA"], 1),
        ("What is the capital of Spain?", ["BARCELONA", "MADRID", "SEVILLE", "VALENCIA"], 1),
        ("Which is the largest lake?", ["LAKE SUPERIOR", "CASPIAN SEA", "LAKE VICTORIA", "LAKE MICHIGAN"], 1),
        ("What is the capital of Germany?", ["MUNICH", "HAMBURG", "BERLIN", "FRANKFURT"], 2),
        ("Which country has the most time zones?", ["USA", "RUSSIA", "CANADA", "FRANCE"], 3),
        ("What is the capital of India?", ["MUMBAI", "NEW DELHI", "KOLKATA", "BANGALORE"], 1),
        ("Which is the largest island?", ["BORNEO", "MADAGASCAR", "GREENLAND", "NEW GUINEA"], 2),
        ("What is the capital of China?", ["SHANGHAI", "BEIJING", "HONG KONG", "GUANGZHOU"], 1),
        ("Which country is also a continent?", ["GREENLAND", "AUSTRALIA", "MADAGASCAR", "ICELAND"], 1),
        ("What is the capital of Russia?", ["ST PETERSBURG", "MOSCOW", "KIEV", "VLADIVOSTOK"], 1),
        ("Which is the smallest ocean?", ["INDIAN", "ATLANTIC", "ARCTIC", "SOUTHERN"], 2),
        ("What is the capital of Turkey?", ["ISTANBUL", "ANKARA", "IZMIR", "BURSA"], 1),
        ("Which mountain range is the longest?", ["ROCKIES", "ANDES", "HIMALAYAS", "ALPS"], 1),
        ("What is the capital of Thailand?", ["PHUKET", "BANGKOK", "CHIANG MAI", "PATTAYA"], 1),
        ("Which is the largest rainforest?", ["CONGO", "AMAZON", "DAINTREE", "SUNDARBANS"], 1),
        ("What is the capital of Argentina?", ["CORDOBA", "BUENOS AIRES", "ROSARIO", "MENDOZA"], 1),
        ("Which country has the most volcanoes?", ["JAPAN", "INDONESIA", "USA", "PHILIPPINES"], 1),
        ("What is the capital of South Africa?", ["JOHANNESBURG", "PRETORIA", "CAPE TOWN", "DURBAN"], 1),
        ("Which is the longest mountain range?", ["ROCKIES", "ANDES", "HIMALAYAS", "ALPS"], 1),
        ("What is the capital of Mexico?", ["GUADALAJARA", "MEXICO CITY", "MONTERREY", "CANCUN"], 1),
        ("Which country has the most UNESCO sites?", ["FRANCE", "ITALY", "CHINA", "SPAIN"], 1),
        ("What is the capital of Saudi Arabia?", ["MECCA", "RIYADH", "JEDDAH", "MEDINA"], 1),
        ("Which is the smallest continent?", ["EUROPE", "AUSTRALIA", "ANTARCTICA", "SOUTH AMERICA"], 1),
        ("What is the capital of Greece?", ["THESSALONIKI", "ATHENS", "SPARTA", "CORINTH"], 1),
        ("Which country spans two continents?", ["RUSSIA", "TURKEY", "EGYPT", "ALL OF THESE"], 3),
        ("What is the capital of Peru?", ["CUSCO", "LIMA", "AREQUIPA", "TRUJILLO"], 1),
        ("Which is the driest desert?", ["SAHARA", "ATACAMA", "GOBI", "ARABIAN"], 1),
        ("What is the capital of Sweden?", ["GOTHENBURG", "STOCKHOLM", "MALMO", "UPPSALA"], 1),
        ("Which country has the most neighbors?", ["RUSSIA", "CHINA", "BRAZIL", "GERMANY"], 1),
        ("What is the capital of Portugal?", ["PORTO", "LISBON", "FARO", "BRAGA"], 1),
        ("Which is the longest beach?", ["COPACABANA", "COX'S BAZAR", "BONDI", "MIAMI"], 1),
    ],
    "SPORTS": [
        ("How many players in a football team?", ["10", "11", "12", "13"], 1),
        ("Who has won the most Grand Slams in tennis?", ["ROGER FEDERER", "RAFAEL NADAL", "NOVAK DJOKOVIC", "PETE SAMPRAS"], 2),
        ("Which country won FIFA World Cup 2018?", ["BRAZIL", "GERMANY", "FRANCE", "ARGENTINA"], 2),
        ("How many rings are in the Olympic logo?", ["4", "5", "6", "7"], 1),
        ("Who is known as God of Cricket?", ["VIRAT KOHLI", "SACHIN TENDULKAR", "MS DHONI", "RICKY PONTING"], 1),
        ("In which sport is a shuttlecock used?", ["TENNIS", "SQUASH", "BADMINTON", "TABLE TENNIS"], 2),
        ("How many points for a touchdown in NFL?", ["5", "6", "7", "8"], 1),
        ("Which country hosted Olympics 2020?", ["CHINA", "JAPAN", "SOUTH KOREA", "AUSTRALIA"], 1),
        ("How many Grand Slam tournaments in tennis?", ["3", "4", "5", "6"], 1),
        ("Who won the most NBA championships?", ["MICHAEL JORDAN", "BILL RUSSELL", "LEBRON JAMES", "MAGIC JOHNSON"], 1),
        ("Which sport uses a puck?", ["LACROSSE", "ICE HOCKEY", "FIELD HOCKEY", "CURLING"], 1),
        ("How many players in a basketball team?", ["4", "5", "6", "7"], 1),
        ("Who has the most goals in football history?", ["MESSI", "CRISTIANO RONALDO", "PELE", "MARADONA"], 1),
        ("In which sport do you use a racquet?", ["SQUASH", "BADMINTON", "TENNIS", "ALL OF THESE"], 3),
        ("How many holes in a standard golf course?", ["16", "18", "20", "22"], 1),
        ("Who won FIFA World Cup 2022?", ["FRANCE", "ARGENTINA", "BRAZIL", "GERMANY"], 1),
        ("Which country has won the most Cricket World Cups?", ["INDIA", "AUSTRALIA", "WEST INDIES", "ENGLAND"], 1),
        ("How many points for a field goal in basketball?", ["1", "2", "3", "4"], 2),
        ("Who is the fastest man in the world?", ["USAIN BOLT", "TYSON GAY", "YOHAN BLAKE", "ASAFA POWELL"], 0),
        ("Which sport is played at Wimbledon?", ["CRICKET", "TENNIS", "RUGBY", "FOOTBALL"], 1),
        ("How many players in a cricket team?", ["10", "11", "12", "13"], 1),
        ("Who won the most Olympic gold medals?", ["CARL LEWIS", "MICHAEL PHELPS", "USAIN BOLT", "SIMONE BILES"], 1),
        ("In which sport is the term 'home run' used?", ["CRICKET", "BASEBALL", "SOFTBALL", "ROUNDERS"], 1),
        ("How many sets in a tennis match?", ["2", "3", "5", "VARIES"], 3),
        ("Who has won the most Formula 1 championships?", ["AYRTON SENNA", "MICHAEL SCHUMACHER", "LEWIS HAMILTON", "JUAN MANUEL FANGIO"], 1),
        ("Which country invented football?", ["BRAZIL", "ENGLAND", "SPAIN", "ITALY"], 1),
        ("How many minutes in a football match?", ["80", "90", "100", "120"], 1),
        ("Who is known as The King in football?", ["MARADONA", "PELE", "MESSI", "RONALDO"], 1),
        ("In which sport do you score a 'try'?", ["FOOTBALL", "RUGBY", "CRICKET", "HOCKEY"], 1),
        ("How many innings in a baseball game?", ["7", "8", "9", "10"], 2),
        ("Who won the most Ballon d'Or awards?", ["CRISTIANO RONALDO", "LIONEL MESSI", "MICHEL PLATINI", "JOHAN CRUYFF"], 1),
        ("Which sport uses a net and a ball?", ["TENNIS", "VOLLEYBALL", "BADMINTON", "ALL OF THESE"], 3),
        ("How many players in a volleyball team?", ["5", "6", "7", "8"], 1),
        ("Who is the highest run scorer in ODI cricket?", ["SACHIN TENDULKAR", "VIRAT KOHLI", "RICKY PONTING", "KUMAR SANGAKKARA"], 0),
        ("In which sport is the term 'ace' used?", ["CRICKET", "TENNIS", "BADMINTON", "TABLE TENNIS"], 1),
        ("How many points for a safety in NFL?", ["1", "2", "3", "4"], 1),
        ("Who won the most Wimbledon titles?", ["ROGER FEDERER", "NOVAK DJOKOVIC", "PETE SAMPRAS", "BJORN BORG"], 0),
        ("Which country has won the most FIFA World Cups?", ["ARGENTINA", "BRAZIL", "GERMANY", "ITALY"], 1),
        ("How many strikes for an out in baseball?", ["2", "3", "4", "5"], 1),
        ("Who is known as The Greatest in boxing?", ["MIKE TYSON", "MUHAMMAD ALI", "FLOYD MAYWEATHER", "SUGAR RAY ROBINSON"], 1),
        ("In which sport is the term 'birdie' used?", ["BADMINTON", "GOLF", "CRICKET", "TENNIS"], 1),
        ("How many points for a penalty kick in rugby?", ["1", "2", "3", "4"], 2),
        ("Who won the most Super Bowl titles?", ["JOE MONTANA", "TOM BRADY", "TERRY BRADSHAW", "PEYTON MANNING"], 1),
        ("Which sport uses a bat and ball?", ["CRICKET", "BASEBALL", "SOFTBALL", "ALL OF THESE"], 3),
        ("How many yards is a football field?", ["90", "100", "110", "120"], 1),
        ("Who has the most goals in World Cup history?", ["RONALDO", "MIROSLAV KLOSE", "PELE", "JUST FONTAINE"], 1),
        ("In which sport is the term 'slam dunk' used?", ["VOLLEYBALL", "BASKETBALL", "HANDBALL", "WATER POLO"], 1),
        ("How many periods in an ice hockey game?", ["2", "3", "4", "5"], 1),
        ("Who is the highest wicket taker in Test cricket?", ["SHANE WARNE", "MUTTIAH MURALITHARAN", "JAMES ANDERSON", "ANIL KUMBLE"], 1),
        ("Which sport uses a mallet and ball?", ["CRICKET", "POLO", "HOCKEY", "LACROSSE"], 1),
    ],
    "LITERATURE": [
        ("Who wrote 'Romeo and Juliet'?", ["CHARLES DICKENS", "WILLIAM SHAKESPEARE", "JANE AUSTEN", "MARK TWAIN"], 1),
        ("Who wrote 'Harry Potter'?", ["J.R.R. TOLKIEN", "C.S. LEWIS", "J.K. ROWLING", "ROALD DAHL"], 2),
        ("What is the first book of the Bible?", ["EXODUS", "GENESIS", "LEVITICUS", "NUMBERS"], 1),
        ("Who wrote '1984'?", ["ALDOUS HUXLEY", "RAY BRADBURY", "GEORGE ORWELL", "KURT VONNEGUT"], 2),
        ("Which book features Sherlock Holmes?", ["DRACULA", "A STUDY IN SCARLET", "FRANKENSTEIN", "THE INVISIBLE MAN"], 1),
        ("Who wrote 'Pride and Prejudice'?", ["EMILY BRONTE", "JANE AUSTEN", "CHARLOTTE BRONTE", "MARY SHELLEY"], 1),
        ("What is the longest epic poem?", ["ODYSSEY", "ILIAD", "MAHABHARATA", "AENEID"], 2),
        ("Who wrote 'The Great Gatsby'?", ["ERNEST HEMINGWAY", "F. SCOTT FITZGERALD", "JOHN STEINBECK", "WILLIAM FAULKNER"], 1),
        ("Who wrote 'To Kill a Mockingbird'?", ["HARPER LEE", "TONI MORRISON", "MAYA ANGELOU", "ALICE WALKER"], 0),
        ("Which book features Atticus Finch?", ["THE CATCHER IN THE RYE", "TO KILL A MOCKINGBIRD", "THE GRAPES OF WRATH", "OF MICE AND MEN"], 1),
        ("Who wrote 'The Lord of the Rings'?", ["C.S. LEWIS", "J.R.R. TOLKIEN", "GEORGE R.R. MARTIN", "TERRY PRATCHETT"], 1),
        ("Which book features Holden Caulfield?", ["THE GREAT GATSBY", "THE CATCHER IN THE RYE", "ON THE ROAD", "FAHRENHEIT 451"], 1),
        ("Who wrote 'Moby Dick'?", ["NATHANIEL HAWTHORNE", "HERMAN MELVILLE", "EDGAR ALLAN POE", "JAMES FENIMORE COOPER"], 1),
        ("Which book features Captain Ahab?", ["TREASURE ISLAND", "MOBY DICK", "20000 LEAGUES", "THE OLD MAN AND THE SEA"], 1),
        ("Who wrote 'The Odyssey'?", ["VIRGIL", "HOMER", "SOPHOCLES", "EURIPIDES"], 1),
        ("Which book features Odysseus?", ["THE ILIAD", "THE ODYSSEY", "THE AENEID", "METAMORPHOSES"], 1),
        ("Who wrote 'Hamlet'?", ["CHRISTOPHER MARLOWE", "WILLIAM SHAKESPEARE", "BEN JONSON", "JOHN MILTON"], 1),
        ("Which play features the ghost of a king?", ["MACBETH", "HAMLET", "OTHELLO", "KING LEAR"], 1),
        ("Who wrote 'Jane Eyre'?", ["EMILY BRONTE", "CHARLOTTE BRONTE", "ANNE BRONTE", "JANE AUSTEN"], 1),
        ("Which book features Mr. Rochester?", ["WUTHERING HEIGHTS", "JANE EYRE", "PRIDE AND PREJUDICE", "EMMA"], 1),
        ("Who wrote 'The Hobbit'?", ["C.S. LEWIS", "J.R.R. TOLKIEN", "LLOYD ALEXANDER", "URSULA K. LE GUIN"], 1),
        ("Which book features Bilbo Baggins?", ["THE HOBBIT", "LORD OF THE RINGS", "THE SILMARILLION", "FARMER GILES"], 0),
        ("Who wrote 'Frankenstein'?", ["BRAM STOKER", "MARY SHELLEY", "EDGAR ALLAN POE", "H.G. WELLS"], 1),
        ("Which book features Victor Frankenstein?", ["DRACULA", "FRANKENSTEIN", "DR JEKYLL AND MR HYDE", "THE INVISIBLE MAN"], 1),
        ("Who wrote 'War and Peace'?", ["FYODOR DOSTOEVSKY", "LEO TOLSTOY", "ANTON CHEKHOV", "IVAN TURGENEV"], 1),
        ("Which book is set during Napoleonic Wars?", ["ANNA KARENINA", "WAR AND PEACE", "THE IDIOT", "CRIME AND PUNISHMENT"], 1),
        ("Who wrote 'The Divine Comedy'?", ["PETRARCH", "DANTE", "BOCCACCIO", "VIRGIL"], 1),
        ("Which book describes Hell, Purgatory, and Paradise?", ["PARADISE LOST", "THE DIVINE COMEDY", "FAERIE QUEENE", "CANTERBURY TALES"], 1),
        ("Who wrote 'Don Quixote'?", ["LOPE DE VEGA", "MIGUEL DE CERVANTES", "CALDERON", "TIRSO DE MOLINA"], 1),
        ("Which book features a windmill fight?", ["GULLIVER'S TRAVELS", "DON QUIXOTE", "CANDIDE", "ROBINSON CRUSOE"], 1),
        ("Who wrote 'The Canterbury Tales'?", ["WILLIAM LANGLAND", "GEOFFREY CHAUCER", "JOHN GOWER", "THOMAS MALORY"], 1),
        ("Which book features pilgrims telling stories?", ["DECAMERON", "CANTERBURY TALES", "ARABIAN NIGHTS", "FRAME TALES"], 1),
        ("Who wrote 'Paradise Lost'?", ["EDMUND SPENSER", "JOHN MILTON", "JOHN DONNE", "ANDREW MARVELL"], 1),
        ("Which book features Satan as a character?", ["FAUST", "PARADISE LOST", "THE DIVINE COMEDY", "DR FAUSTUS"], 1),
        ("Who wrote 'One Hundred Years of Solitude'?", ["JORGE LUIS BORGES", "GABRIEL GARCIA MARQUEZ", "PABLO NERUDA", "OCTAVIO PAZ"], 1),
        ("Which book features the Buendia family?", ["THE HOUSE OF SPIRITS", "ONE HUNDRED YEARS", "LOVE IN TIME OF CHOLERA", "CHRONICLE OF DEATH"], 1),
        ("Who wrote 'Crime and Punishment'?", ["LEO TOLSTOY", "FYODOR DOSTOEVSKY", "ANTON CHEKHOV", "NIKOLAI GOGOL"], 1),
        ("Which book features Raskolnikov?", ["THE IDIOT", "CRIME AND PUNISHMENT", "THE BROTHERS KARAMAZOV", "DEMONS"], 1),
        ("Who wrote 'The Picture of Dorian Gray'?", ["OSCAR WILDE", "H.G. WELLS", "ROBERT LOUIS STEVENSON", "BRAM STOKER"], 0),
        ("Which book features a portrait that ages?", ["JEKYLL AND HYDE", "DORIAN GRAY", "PHANTOM OF OPERA", "DRACULA"], 1),
        ("Who wrote 'Brave New World'?", ["GEORGE ORWELL", "ALDOUS HUXLEY", "RAY BRADBURY", "KURT VONNEGUT"], 1),
        ("Which book features soma drug?", ["1984", "BRAVE NEW WORLD", "FAHRENHEIT 451", "CLOCKWORK ORANGE"], 1),
        ("Who wrote 'The Grapes of Wrath'?", ["WILLIAM FAULKNER", "JOHN STEINBECK", "ERNEST HEMINGWAY", "F. SCOTT FITZGERALD"], 1),
        ("Which book features the Joad family?", ["OF MICE AND MEN", "THE GRAPES OF WRATH", "EAST OF EDEN", "CANNERY ROW"], 1),
        ("Who wrote 'Catch-22'?", ["KURT VONNEGUT", "JOSEPH HELLER", "NORMAN MAILER", "JAMES JONES"], 1),
        ("Which book is set during World War II?", ["SLAUGHTERHOUSE FIVE", "CATCH-22", "THE NAKED AND THE DEAD", "ALL OF THESE"], 3),
        ("Who wrote 'The Old Man and the Sea'?", ["JOHN STEINBECK", "ERNEST HEMINGWAY", "WILLIAM FAULKNER", "F. SCOTT FITZGERALD"], 1),
        ("Which book features Santiago the fisherman?", ["MOBY DICK", "THE OLD MAN AND THE SEA", "20000 LEAGUES", "LIFE OF PI"], 1),
        ("Who wrote 'Alice in Wonderland'?", ["LEWIS CARROLL", "ROALD DAHL", "C.S. LEWIS", "J.M. BARRIE"], 0),
        ("Which book features the Cheshire Cat?", ["PETER PAN", "ALICE IN WONDERLAND", "WIZARD OF OZ", "NARNIA"], 1),
        ("Who wrote 'Dracula'?", ["MARY SHELLEY", "BRAM STOKER", "EDGAR ALLAN POE", "H.P. LOVECRAFT"], 1),
    ]
}

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, text_color=WHITE):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.is_hovered = False

    def draw(self, screen, font):
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, color, self.rect, border_radius=15)
        pygame.draw.rect(screen, WHITE, self.rect, 3, border_radius=15)
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def is_clicked(self, mouse_pos, mouse_click):
        return self.rect.collidepoint(mouse_pos) and mouse_click

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Quiz Master")
        self.clock = pygame.time.Clock()
        self.running = True

        self.title_font = pygame.font.Font(None, 100)
        self.large_font = pygame.font.Font(None, 60)
        self.medium_font = pygame.font.Font(None, 40)
        self.small_font = pygame.font.Font(None, 32)

        self.state = "MENU"
        self.selected_genre = None
        self.questions = []
        self.current_question = 0
        self.score = 0
        self.hearts = 5
        self.high_score = 0 

        self.setup_music()
        self.genre_backgrounds = self.load_backgrounds()

    def setup_music(self):
        """Setup background music"""
        try:
            if os.path.exists("joy-300569.mp3"):
                pygame.mixer.music.load("joy-300569.mp3")
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play(-1)
        except:
            print("No music file found. Add 'joy-300569.mp3' for background music!")

    def load_backgrounds(self):
        """Load and scale background images for each genre"""
        backgrounds = {}
        for genre, path in GENRE_BG_IMAGES.items():
            if os.path.exists(path):
                image = pygame.image.load(path).convert()
                image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
                backgrounds[genre] = image
            else:
                backgrounds[genre] = None
                print(f"Background image for {genre} not found: {path}")
        return backgrounds

    def draw_grid_background(self, color):
        self.screen.fill(color)
        grid_size = 20
        for x in range(0, SCREEN_WIDTH, grid_size):
            pygame.draw.line(self.screen, (color[0] + 10, color[1] + 10, color[2] + 10), (x, 0), (x, SCREEN_HEIGHT), 1)
        for y in range(0, SCREEN_HEIGHT, grid_size):
            pygame.draw.line(self.screen, (color[0] + 10, color[1] + 10, color[2] + 10), (0, y), (SCREEN_WIDTH, y), 1)

    def draw_hearts(self, x, y):
        heart_size = 20
        for i in range(self.hearts):
            pygame.draw.circle(self.screen, RED, (x + i * 50, y), heart_size // 2)
            pygame.draw.circle(self.screen, RED, (x + i * 50 + 10, y), heart_size // 2)
            pygame.draw.polygon(self.screen, RED, [
                (x + i * 50 - 5, y + 5),
                (x + i * 50 + 15, y + 5),
                (x + i * 50 + 5, y + 20)
            ])

    def menu_screen(self):
        self.draw_grid_background(DARK_BLUE)
        title = self.title_font.render("QUIZ MASTER", True, LIGHT_BLUE)
        self.screen.blit(title, title.get_rect(center=(SCREEN_WIDTH // 2, 100)))

        subtitle = self.medium_font.render("SELECT YOUR CHALLENGE", True, WHITE)
        self.screen.blit(subtitle, subtitle.get_rect(center=(SCREEN_WIDTH // 2, 170)))

        high_text = self.medium_font.render(f"HIGH SCORE: {self.high_score}", True, LIGHT_BLUE)
        self.screen.blit(high_text, high_text.get_rect(center=(SCREEN_WIDTH // 2, 220)))

        genres = list(GENRE_COLORS.keys())
        button_width = 300
        button_height = 150
        start_x = (SCREEN_WIDTH - (3 * button_width + 2 * 30)) // 2
        start_y = 250
        buttons = []
        for i, genre in enumerate(genres):
            row, col = divmod(i, 3)
            x = start_x + col * (button_width + 30)
            y = start_y + row * (button_height + 30)
            color = GENRE_COLORS[genre]
            hover_color = tuple(min(c + 30, 255) for c in color)
            button = Button(x, y, button_width, button_height, genre, color, hover_color)
            buttons.append((button, genre))

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()[0]
        for button, genre in buttons:
            button.check_hover(mouse_pos)
            button.draw(self.screen, self.medium_font)
            if button.is_clicked(mouse_pos, mouse_click):
                self.selected_genre = genre
                self.start_game()
                pygame.time.wait(200)

    def start_game(self):
        self.state = "PLAYING"
        self.questions = QUIZ_DATA[self.selected_genre]
        self.current_question = 0
        self.score = 0
        self.hearts = 5

    def playing_screen(self):
        if self.hearts <= 0 or self.current_question >= len(self.questions):
            self.state = "GAME_OVER"
            return

        bg_image = self.genre_backgrounds.get(self.selected_genre)
        if bg_image:
            self.screen.blit(bg_image, (0, 0))
        else:
            self.draw_grid_background(GENRE_BG[self.selected_genre])

      
        bar_rect = pygame.Rect(180, 70, SCREEN_WIDTH - 360, 90)
        pygame.draw.rect(self.screen, DARK_GRAY, bar_rect, border_radius=10)
        pygame.draw.rect(self.screen, WHITE, bar_rect, 3, border_radius=10)
        self.draw_hearts(220, 115)

        score_text = self.medium_font.render("SCORE", True, GRAY)
        self.screen.blit(score_text, (SCREEN_WIDTH // 2 - 80, 85))
        score_num = self.large_font.render(str(self.score), True, LIGHT_BLUE)
        self.screen.blit(score_num, (SCREEN_WIDTH // 2 - 20, 105))

        question_text = self.medium_font.render("QUESTION", True, GRAY)
        self.screen.blit(question_text, (SCREEN_WIDTH - 420, 85))
        question_label = f"{self.current_question + 1} / {len(self.questions)}"
        question_num = self.large_font.render(question_label, True, WHITE)
        num_rect = question_num.get_rect()
        num_rect.topright = (SCREEN_WIDTH - 220, 100)
        self.screen.blit(question_num, num_rect)

        
        question, answers, correct = self.questions[self.current_question]
        question_box = pygame.Rect(180, 200, SCREEN_WIDTH - 360, 350)
        pygame.draw.rect(self.screen, DARK_GRAY, question_box, border_radius=15)
        pygame.draw.rect(self.screen, WHITE, question_box, 3, border_radius=15)

       
        words = question.split()
        lines, current_line = [], ""
        for word in words:
            test_line = current_line + word + " "
            if self.medium_font.size(test_line)[0] < (SCREEN_WIDTH - 400):
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + " "
        lines.append(current_line)

        for i, line in enumerate(lines):
            text_surface = self.medium_font.render(line.strip(), True, WHITE)
            self.screen.blit(text_surface, (200, 230 + i * 40))

        button_width, button_height = 380, 80
        start_x = (SCREEN_WIDTH - (2 * button_width + 30)) // 2
        start_y = 360
        buttons = []
        for i, answer in enumerate(answers):
            x = start_x + (i % 2) * (button_width + 30)
            y = start_y + (i // 2) * (button_height + 20)
            button = Button(x, y, button_width, button_height, answer, DARK_BLUE, (60, 70, 120))
            buttons.append(button)

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()[0]
        clicked = False
        for i, button in enumerate(buttons):
            button.check_hover(mouse_pos)
            button.draw(self.screen, self.small_font)
            if button.is_clicked(mouse_pos, mouse_click) and not clicked:
                clicked = True
                print("clicked index:", i, "correct index:", correct)  # DEBUG
                if i == correct:
                    correct_sound.play()
                    self.score += 1
                else:
                    self.hearts -= 1
                self.current_question += 1
                pygame.time.wait(200)

    def game_over_screen(self):
        
        if self.score > self.high_score:
            self.high_score = self.score

        self.draw_grid_background(DARK_BLUE)
        title = self.title_font.render("GAME OVER", True, RED)
        self.screen.blit(title, title.get_rect(center=(SCREEN_WIDTH // 2, 150)))

        box = pygame.Rect(SCREEN_WIDTH // 2 - 250, 280, 500, 220)
        pygame.draw.rect(self.screen, DARK_GRAY, box, border_radius=15)
        pygame.draw.rect(self.screen, WHITE, box, 3, border_radius=15)

        score_text = self.medium_font.render(f"YOUR SCORE: {self.score}", True, WHITE)
        self.screen.blit(score_text, score_text.get_rect(center=(SCREEN_WIDTH // 2, 320)))

        high_text = self.medium_font.render(f"HIGH SCORE: {self.high_score}", True, LIGHT_BLUE)
        self.screen.blit(high_text, high_text.get_rect(center=(SCREEN_WIDTH // 2, 370)))

        restart_button = Button(
            SCREEN_WIDTH // 2 - 150, 520, 300, 80,
            "PLAY AGAIN", (50, 150, 50), (70, 180, 70)
        )
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()[0]
        restart_button.check_hover(mouse_pos)
        restart_button.draw(self.screen, self.medium_font)
        if restart_button.is_clicked(mouse_pos, mouse_click):
            self.state = "MENU"
            pygame.time.wait(200)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            if self.state == "MENU":
                self.menu_screen()
            elif self.state == "PLAYING":
                self.playing_screen()
            elif self.state == "GAME_OVER":
                self.game_over_screen()
            pygame.display.flip()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()
