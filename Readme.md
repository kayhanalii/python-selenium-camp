@pytest.fixture: Bu dekoratör, test çalıştırma tarafından kullanılmak üzere önceden ayarlanmış bir öğe oluşturur.

@pytest.mark.parametrize: Bu dekoratör, test cihazları farklı armatür çalıştırmaları ile çalıştırmak için kullanılır.

@pytest.mark.parametrize(argnames, argvalues): Bu dekoratör, argnames argümanı ile belirtilen değişken isimleri ve argvalues değişkeni ile belirtilen değişken değerleri listesi kullanılarak parametreleri test etmek için kullanılır.

@pytest.mark.parametrize("arg",[val1 ,val2,...]): Bu dekoratör, bir argümanın farklı değerlerinin test yuvasını kullanarak sağlar.

@pytest.mark.skip: Bu dekoratör, bir testi çalıştırmadan geçmek için kullanılır.

@pytest.mark.xfail: Bu dekoratör, bir testin deneysel başarısız olması durumunda kullanılır.

@pytest.mark.usefixtures: Bu dekoratör, bir test çalıştırma çalışması için gerekli olan bir veya daha fazla araç setini belirler.

@pytest.mark.timeout: Bu dekoratör, bir test uygulamalarının belirli bir süre içinde tamamlanması gerektiğini belirtir.

@pytest.mark.filterwarnings: Bu dekoratör, belirli bir testin çalıştırılması sırasında Python hatalarını yürütmek veya kontrol etmek için kullanılır.
![test_screenshot](https://user-images.githubusercontent.com/125891146/229102880-39018a14-eab8-40f6-bd7f-44cf8b5b5d36.png)
