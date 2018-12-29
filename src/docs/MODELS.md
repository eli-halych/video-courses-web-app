Model Architecture planning

Membership
      -slug <!-- better than IDs for dynamically generated pages and URLs,like /course-number-1/ -->
      -type (free, pro, enterprise)
      -price
      -stripe plan id

UserMembership
      -user                     (FK to default user)
      -stripe customer id
      -membership type          (FK to Membership)

Subscription
      -user membership          (FK to UserMembership)
      -stripe subscription id
      -active



Course
      -slug
      -title
      -description
      -allowed memberships    (ManyToManyField to Membership)

Lesson
      -slug
      -title
      -Course                 (FK to Course)
      -position               
      -video
      -thumbnail
