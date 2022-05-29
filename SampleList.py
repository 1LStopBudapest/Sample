import os, sys

bkgs = ['WJets', 'ttbar', 'SingleTop', 'DY', 'Zinv', 'QCD', 'VV', 'TTX']

data = ['Data']


signals = ['1076_1016', '1076_1024', '1076_1036', '1076_1044', '1076_1056', '1076_1064', '1076_996', '1100_1020', '1100_1032', '1100_1040', '1100_1052', '1100_1060', '1100_1072', '1100_1080', '1100_1092', '250_170', '250_180', '250_190', '250_200', '250_210', '250_220', '250_230', '250_240', '275_195', '275_205', '275_215', '275_225', '275_235', '275_245', '275_255', '275_265', '300_220', '300_230', '300_240', '300_250', '300_260', '300_270', '300_280', '300_290', '325_245', '325_255', '325_265', '325_275', '325_285', '325_295', '325_305', '325_315', '350_270', '350_280', '350_290', '350_300', '350_310', '350_320', '350_330', '350_340', '375_295', '375_305', '375_315', '375_325', '375_335', '375_345', '375_355', '375_365', '400_320', '400_330', '400_340', '400_350', '400_360', '400_370', '400_380', '400_390', '425_345', '425_355', '425_365', '425_375', '425_385', '425_395', '425_405', '425_415', '450_370', '450_380', '450_390', '450_400', '450_410', '450_420', '450_430', '450_440', '475_395', '475_405', '475_415', '475_425', '475_435', '475_445', '475_455', '475_465', '500_420', '500_430', '500_440', '500_450', '500_460', '500_470', '500_480', '500_490', '526_445', '526_455', '526_465', '526_475', '526_485', '526_495', '526_505', '526_516', '550_470', '550_480', '550_490', '550_500', '550_510', '550_520', '550_530', '550_540', '576_495', '576_505', '576_516', '576_526', '576_536', '576_546', '576_556', '576_566', '600_520', '600_530', '600_540', '600_550', '600_560', '600_570', '600_580', '600_590', '626_546', '626_556', '626_566', '626_576', '626_586', '626_596', '626_606', '626_616', '650_570', '650_580', '650_590', '650_600', '650_610', '650_620', '650_630', '650_640', '676_596', '676_606', '676_616', '676_626', '676_636', '676_646', '676_656', '676_666', '700_620', '700_630', '700_640', '700_650', '700_660', '700_670', '700_680', '700_690', '726_646', '726_656', '726_666', '726_676', '726_686', '726_696', '726_706', '726_716', '750_670', '750_680', '750_690', '750_700', '750_710', '750_720', '750_730', '750_740', '776_696', '776_706', '776_716', '776_726', '776_736', '776_746', '776_756', '776_766', '800_720', '800_730', '800_740', '800_750', '800_760', '800_770', '800_780', '800_790', '826_746', '826_756', '826_766', '826_776', '826_786', '826_796', '826_806', '826_816', '850_770', '850_780', '850_790', '850_800', '850_810', '850_820', '850_830', '850_840', '876_796', '876_806', '876_816', '876_826', '876_836', '876_846', '876_856', '876_866', '900_820', '900_830', '900_840', '900_850', '900_860', '900_870', '900_880', '900_890', '926_846', '926_856', '926_866', '926_876', '926_886', '926_896', '926_906', '926_916', '950_870', '950_880', '950_890', '950_900', '950_910', '950_920', '950_930', '950_940', '976_896', '976_906', '976_916', '976_926', '976_936', '976_946', '976_956', '976_966']

snameMap = {'ttbar':'TTbar', 'SingleTop':'ST', 'WJets':'WJetsToLNu', 'TTX':'TTV', 'Zinv':'ZJetsToNuNu', 'DY':'DYJetsToLL', 'QCD':'QCD', 'VV':'VV', 'Data':'MET_Data'}

