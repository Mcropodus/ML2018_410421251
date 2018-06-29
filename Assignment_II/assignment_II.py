import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
import scipy

# The digits dataset
digits = datasets.load_digits()


images_and_labels = list(zip(digits.images, digits.target))
for index, (image, label) in enumerate(images_and_labels[:4]):
    plt.subplot(2, 4, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Training: %i' % label)

sample = len(digits.images)
data = digits.images.reshape((sample, -1))

classifier = svm.SVC(gamma=0.001)
classifier.fit(data[:sample // 2], digits.target[:sample // 2])

expected = digits.target[sample // 2:]
predicted = classifier.predict(data[sample // 2:])

print("Report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(expected, predicted)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))


images_and_predictions = list(zip(digits.images[sample // 2:], predicted))
for index, (image, prediction) in enumerate(images_and_predictions[:4]):
    plt.subplot(2, 4, index + 5)
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Prediction: %i' % prediction)

plt.show()

