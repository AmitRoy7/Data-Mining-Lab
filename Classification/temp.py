from matplotlib import pyplot as plt
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
import numpy as np



y_true = np.array(['a', 'b', 'c', 'd'])
y_score = np.array(['a', 'c', 'e', 'f'])


fpr, tpr, thresholds = roc_curve(y_true, y_score, pos_label=4)
roc_auc = auc(y_true, y_score)

# Plot ROC curve
plt.plot(fpr, tpr, label='ROC curve (area = %0.3f)' % roc_auc)
plt.plot([0, 1], [0, 1], 'k--')  # random predictions curve
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('False Positive Rate or (1 - Specifity)')
plt.ylabel('True Positive Rate or (Sensitivity)')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()
