
# Penguins Dataset Analysis

## Dataset Overview
- **Shape**: (344, 7)
- **Columns**: ['species', 'island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex']

## Basic Statistics
|       |   bill_length_mm |   bill_depth_mm |   flipper_length_mm |   body_mass_g |
|:------|-----------------:|----------------:|--------------------:|--------------:|
| count |        342       |       342       |            342      |       342     |
| mean  |         43.9219  |        17.1512  |            200.915  |      4201.75  |
| std   |          5.45958 |         1.97479 |             14.0617 |       801.955 |
| min   |         32.1     |        13.1     |            172      |      2700     |
| 25%   |         39.225   |        15.6     |            190      |      3550     |
| 50%   |         44.45    |        17.3     |            197      |      4050     |
| 75%   |         48.5     |        18.7     |            213      |      4750     |
| max   |         59.6     |        21.5     |            231      |      6300     |

## Missing Values
|                   |   0 |
|:------------------|----:|
| species           |   0 |
| island            |   0 |
| bill_length_mm    |   2 |
| bill_depth_mm     |   2 |
| flipper_length_mm |   2 |
| body_mass_g       |   2 |
| sex               |  11 |

## Visualizations

### 1. Histogram of Bill Length
![Histogram of Bill Length](hist_bill_length.png)

**인사이트**: 이 히스토그램은 펭귄의 부리 길이 분포를 보여줍니다. 평균 부리 길이는 약 43.9mm로, 대부분의 펭귄이 39-48mm 범위에 집중되어 있습니다. 분포는 정규분포에 가까우며, 종별 차이를 고려할 때 Adelie 종이 상대적으로 짧고 Gentoo 종이 긴 경향을 보입니다. 이는 먹이 습성과 서식지 적응의 차이를 반영할 수 있습니다. 결측치가 2개 있어 전체 데이터를 대표하지 않을 수 있으나, 큰 영향을 미치지 않습니다. (약 150자)

### 2. Histogram of Bill Depth
![Histogram of Bill Depth](hist_bill_depth.png)

**인사이트**: 부리 깊이의 히스토그램은 평균 17.15mm로, 펭귄 종간 차이를 잘 보여줍니다. Adelie 종은 깊이가 깊고, Gentoo 종은 얕은 경향이 있어 먹이 포획 방식의 차이를 시사합니다. 분포는 약간 왼쪽으로 치우쳐 있으며, 결측치가 부리 길이와 동일하게 2개입니다. 이 지표는 펭귄의 생태적 역할을 이해하는 데 유용합니다. (약 120자)

### 3. Histogram of Flipper Length
![Histogram of Flipper Length](hist_flipper_length.png)

**인사이트**: 플리퍼 길이 히스토그램은 평균 200.9mm로, 펭귄의 수영 능력을 나타냅니다. Gentoo 종이 가장 긴 플리퍼를 가지고 있어 깊은 바다에서 사냥하는 데 적합하며, Adelie와 Chinstrap은 상대적으로 짧습니다. 분포는 정규에 가까우나, 종별로 명확한 차이를 보입니다. 결측치 2개로 데이터 신뢰성이 높습니다. (약 130자)

### 4. Histogram of Body Mass
![Histogram of Body Mass](hist_body_mass.png)

**인사이트**: 몸무게 히스토그램은 평균 4201g로, 펭귄의 크기를 보여줍니다. Gentoo 종이 가장 무거워 에너지 저장 능력이 뛰어나며, Adelie는 가볍습니다. 분포는 오른쪽으로 약간 치우쳐 있어 큰 펭귄이 적은 비율을 차지합니다. 결측치 2개로, 종별 생존 전략을 분석하는 데 중요합니다. (약 110자)

### 5. Boxplot of Bill Length by Species
![Boxplot of Bill Length by Species](box_bill_length_species.png)

**인사이트**: 종별 부리 길이 박스플롯은 Gentoo가 가장 길고(평균 47.5mm), Adelie가 짧습니다(38.8mm). Chinstrap은 중간. 이상치가 적어 데이터 일관성이 높습니다. 이는 먹이원 차이를 반영하며, 생태적 niche를 이해하는 데 도움이 됩니다. 결측치로 인한 약간의 편향 가능성. (약 120자)

### 6. Boxplot of Bill Depth by Species
![Boxplot of Bill Depth by Species](box_bill_depth_species.png)

**인사이트**: 부리 깊이 박스플롯은 Adelie가 가장 깊고(18.3mm), Gentoo가 얕습니다(15.0mm). 이는 포식 방식의 차이를 보여줍니다. Chinstrap은 중간. 분산이 작아 종내 일관성이 높습니다. 이상치가 거의 없어 신뢰할 수 있습니다. 생태 연구에 유용. (약 100자)

### 7. Scatter Plot of Bill Length vs Bill Depth
![Scatter Plot of Bill Length vs Bill Depth](scatter_bill_length_depth.png)

**인사이트**: 부리 길이와 깊이의 스캐터플롯은 약한 부정 상관을 보입니다. 종별로 명확히 분리되며, Adelie는 깊고 짧은 부리, Gentoo는 얕고 긴 부리를 가집니다. 이는 먹이 적응의 진화를 나타냅니다. 클러스터링이 잘 되어 있어 분류 모델에 유용합니다. (약 110자)

### 8. Scatter Plot of Flipper Length vs Body Mass
![Scatter Plot of Flipper Length vs Body Mass](scatter_flipper_body_mass.png)

**인사이트**: 플리퍼 길이와 몸무게의 스캐터플롯은 강한 양의 상관(약 0.87)을 보여줍니다. 큰 펭귄이 긴 플리퍼를 가지며, 수영 효율성을 높입니다. Gentoo가 우상단에 집중되어 있습니다. 이는 생물학적 scaling 법칙을 따르며, 환경 적응을 분석하는 데 중요합니다. (약 120자)

### 9. Count of Species (Bar Chart)
![Count of Species](count_species.png)

**인사이트**: 종별 개수 바 차트는 Adelie가 152마리로 가장 많고, Gentoo 124, Chinstrap 68입니다. 이는 서식지 선호도를 반영합니다. Adelie는 모든 섬에 분포하지만 Gentoo는 Biscoe에 집중. 인구 동역학 연구에 기초 자료입니다. (약 100자)

#### Cross-tabulation for Bar Chart (Species Count)
| species   |   Biscoe |   Dream |   Torgersen |
|:----------|---------:|--------:|------------:|
| Adelie    |       44 |      56 |          52 |
| Chinstrap |        0 |      68 |           0 |
| Gentoo    |      124 |       0 |           0 |

**인사이트**: 교차표는 종과 섬의 관계를 보여줍니다. Gentoo는 Biscoe에만, Chinstrap은 Dream에만 서식합니다. Adelie는 균등 분포. 이는 섬별 환경 차이로 인한 niche 분할을 시사합니다. 보존 전략 수립에 유용합니다. (약 110자)

#### Pivot Table for Bar Chart (Mean Body Mass by Species and Island)
| species   |   Biscoe |   Dream |   Torgersen |
|:----------|---------:|--------:|------------:|
| Adelie    |  3709.66 | 3688.39 |     3706.37 |
| Chinstrap |   nan    | 3733.09 |      nan    |
| Gentoo    |  5076.02 |  nan    |      nan    |

**인사이트**: 피봇테이블은 평균 몸무게를 종과 섬별로 보여줍니다. Gentoo의 Biscoe 평균이 5076g으로 높고, Adelie는 섬간 차이가 적습니다. 이는 영양 공급 차이를 나타내며, 기후 변화 영향 평가에 도움이 됩니다. (약 100자)

### 10. Mean Body Mass by Species (Bar Chart)
![Mean Body Mass by Species](bar_body_mass_species.png)

**인사이트**: 평균 몸무게 바 차트는 Gentoo가 5076g으로 가장 무거우며, Adelie 3703g, Chinstrap 3733g입니다. 이는 서식지 자원 차이를 반영합니다. Gentoo의 높은 몸무게는 더 깊은 바다 사냥을 가능하게 합니다. 종간 경쟁과 적응을 이해하는 데 필수적입니다. (약 120자)

### 11. Pair Plot
![Pair Plot](pairplot.png)

**인사이트**: 페어플롯은 모든 수치 변수 간 관계를 종별로 색상 구분하여 보여줍니다. 부리 길이와 깊이는 부정 상관, 플리퍼와 몸무게는 강한 양의 상관입니다. 종별 클러스터링이 명확해 분류에 유용합니다. 이상치가 적어 데이터 품질이 좋습니다. 종합적 생태 분석에 이상적입니다. (약 130자)

### 12. Violin Plot of Bill Length by Species
![Violin Plot of Bill Length by Species](violin_bill_length_species.png)

**인사이트**: 바이올린 플롯은 부리 길이의 분포 밀도를 종별로 보여줍니다. Gentoo의 분포가 넓고 Adelie가 좁습니다. 중앙값과 분산을 동시에 볼 수 있어 박스플롯보다 풍부한 정보를 제공합니다. 종별 진화적 차이를 시각화합니다. 연구에서 분포 형태 분석에 유용합니다. (약 120자)

### 13. Correlation Heatmap
![Correlation Heatmap](heatmap_corr.png)

**인사이트**: 상관 히트맵은 변수 간 선형 관계를 보여줍니다. 플리퍼 길이와 몸무게가 0.87로 강한 양의 상관, 부리 길이와 깊이가 -0.23으로 약한 부정 상관입니다. 다른 변수들은 약한 상관. 이는 펭귄의 형태적 적응을 나타내며, 다중공선성 검토에 중요합니다. (약 120자)

### 14. Count of Islands (Bar Chart)
![Count of Islands](count_island.png)

**인사이트**: 섬별 개수 바 차트는 Biscoe가 168마리로 가장 많고, Dream 124, Torgersen 52입니다. 이는 Gentoo의 Biscoe 집중 때문입니다. 섬별 환경 차이가 인구 분포를 결정합니다. 기후 변화 연구에서 섬별 영향 평가에 기초가 됩니다. (약 100자)

### 15. Boxplot of Body Mass by Island
![Boxplot of Body Mass by Island](box_body_mass_island.png)

**인사이트**: 섬별 몸무게 박스플롯은 Biscoe가 평균 4716g으로 높고, Dream과 Torgersen이 비슷합니다. 이는 Gentoo의 존재 때문입니다. Biscoe의 분산이 크며, 이상치가 있습니다. 섬별 자원 차이를 반영하며, 보존 우선순위 설정에 도움이 됩니다. (약 110자)
