############
curve module
############

.. |eacute| unicode:: U+000E9 .. LATIN SMALL LETTER E WITH ACUTE
   :trim:

This is a collection of procedures for performing computations on a
B |eacute| zier `curve`_.

.. _curve: https://en.wikipedia.org/wiki/B%C3%A9zier_curve

**********
Procedures
**********

.. c:function:: void compute_length(int *num_nodes, \
                                    int *dimension, \
                                    double *nodes, \
                                    double *length, \
                                    int *error_val)

   Computes the length of a B |eacute| zier curve via

   .. math::

      \ell = \int_0^1 \left\lVert B'(s) \right\rVert \, ds.

   :param int* num_nodes:
      **[Input]** The number of control points :math:`N` of a
      B |eacute| zier curve.
   :param int* dimension:
      **[Input]** The dimension :math:`D` such that the curve lies in
      :math:`\mathbf{R}^D`.
   :param double* nodes:
      **[Input]** The actual control points of the curve as a
      :math:`D \times N` array. This should be laid out in Fortran order,
      with :math:`D N` total values.
   :param double* length:
      **[Output]** The computed length :math:`\ell`.
   :param int* error_val:
      **[Output]** An error status passed along from ``dqagse`` (a QUADPACK
      procedure).

   **Signature:**

   .. code-block:: c

      void
      compute_length(int *num_nodes,
                     int *dimension,
                     double *nodes,
                     double *length,
                     int *error_val);

.. c:function:: void elevate_nodes_curve(int *num_nodes, \
                                         int *dimension, \
                                         double *nodes, \
                                         double *elevated)

   Degree-elevate a B |eacute| zier curve. Does so by producing
   control points of a higher degree that define the exact same curve.

   See :meth:`.Curve.elevate` for more details.

   :param int* num_nodes:
      **[Input]** The number of control points :math:`N` of a
      B |eacute| zier curve.
   :param int* dimension:
      **[Input]** The dimension :math:`D` such that the curve lies in
      :math:`\mathbf{R}^D`.
   :param double* nodes:
      **[Input]** The actual control points of the curve as a
      :math:`D \times N` array. This should be laid out in Fortran order,
      with :math:`D N` total values.
   :param double* elevated:
      **[Output]** The control points of the degree-elevated curve as a
      :math:`D \times (N + 1)` array, laid out in Fortran order.

   **Signature:**

   .. code-block:: c

      void
      elevate_nodes_curve(int *num_nodes,
                          int *dimension,
                          double *nodes,
                          double *elevated);

.. c:function:: void evaluate_curve_barycentric(int *num_nodes, \
                                                int *dimension, \
                                                double *nodes, \
                                                int *num_vals, \
                                                double *lambda1, \
                                                double *lambda2, \
                                                double *evaluated)

   For a B |eacute| zier curve with control points :math:`p_0, \ldots, p_d`,
   this evaluates the quantity

   .. math::

      Q(\lambda_1, \lambda_2) =
          \sum_{j = 0}^d \binom{d}{j} \lambda_1^{d - j} \lambda_2^j p_j.

   The typical case is barycentric, i.e. :math:`\lambda_1 + \lambda_2 = 1`, but
   this is not required.

   :param int* num_nodes:
      **[Input]** The number of control points :math:`N` of a
      B |eacute| zier curve.
   :param int* dimension:
      **[Input]** The dimension :math:`D` such that the curve lies in
      :math:`\mathbf{R}^D`.
   :param double* nodes:
      **[Input]** The actual control points of the curve as a
      :math:`D \times N` array. This should be laid out in Fortran order,
      with :math:`D N` total values.
   :param int* num_vals:
      **[Input]** The number of values :math:`k` where the quantity will be
      evaluated.
   :param double* lambda1:
      **[Input]** An array of :math:`k` values used for the first parameter
      :math:`\lambda_1`.
   :param double* lambda2:
      **[Input]** An array of :math:`k` values used for the first parameter
      :math:`\lambda_2`.
   :param double* evaluated:
      **[Output]** The evaluated quantites as a :math:`D \times k` array, laid
      out in Fortran order. Column :math:`j` of ``evaluated`` will contain
      :math:`Q\left(\lambda_1\left[j\right], \lambda_2\left[j\right]\right)`.

   **Signature:**

   .. code-block:: c

      void
      evaluate_curve_barycentric(int *num_nodes,
                                 int *dimension,
                                 double *nodes,
                                 int *num_vals,
                                 double *lambda1,
                                 double *lambda2,
                                 double *evaluated);

.. c:function:: void evaluate_hodograph(double *s, \
                                        int *num_nodes, \
                                        int *dimension, \
                                        double *nodes, \
                                        double *hodograph)

   Evaluates the hodograph (or derivative) of a B |eacute| ezier curve
   function :math:`B'(s)`.

   :param int* num_nodes:
      **[Input]** The number of control points :math:`N` of a
      B |eacute| zier curve.
   :param int* dimension:
      **[Input]** The dimension :math:`D` such that the curve lies in
      :math:`\mathbf{R}^D`.
   :param double* nodes:
      **[Input]** The actual control points of the curve as a
      :math:`D \times N` array. This should be laid out in Fortran order,
      with :math:`D N` total values.
   :param double* hodograph:
      **[Output]** The hodograph :math:`B'(s)` as a :math:`D \times 1` array.

   **Signature:**

   .. code-block:: c

      void
      evaluate_hodograph(double *s,
                         int *num_nodes,
                         int *dimension,
                         double *nodes,
                         double *hodograph);

.. c:function:: void evaluate_multi(int *num_nodes, \
                                    int *dimension, \
                                    double *nodes, \
                                    int *num_vals, \
                                    double *s_vals, \
                                    double *evaluated)

   Evaluate a B |eacute| zier curve function :math:`B(s_j)` at
   multiple values :math:`\left\{s_j\right\}_j`.

   :param int* num_nodes:
      **[Input]** The number of control points :math:`N` of a
      B |eacute| zier curve.
   :param int* dimension:
      **[Input]** The dimension :math:`D` such that the curve lies in
      :math:`\mathbf{R}^D`.
   :param double* nodes:
      **[Input]** The actual control points of the curve as a
      :math:`D \times N` array. This should be laid out in Fortran order,
      with :math:`D N` total values.
   :param int* num_vals:
      **[Input]** The number of values :math:`k` where the :math:`B(s)` will be
      evaluated.
   :param double* s_vals:
      **[Input]** An array of :math:`k` values :math:`s_j`.
   :param double* evaluated:
      **[Output]** The evaluated points as a :math:`D \times k` array, laid
      out in Fortran order. Column :math:`j` of ``evaluated`` will contain
      :math:`B\left(s_j\right)`.

   **Signature:**

   .. code-block:: c

      void
      evaluate_multi(int *num_nodes,
                     int *dimension,
                     double *nodes,
                     int *num_vals,
                     double *s_vals,
                     double *evaluated);

.. c:function:: void full_reduce(int *num_nodes, \
                                 int *dimension, \
                                 double *nodes, \
                                 int *num_reduced_nodes, \
                                 double *reduced, \
                                 bool *not_implemented)

   Perform a "full" degree reduction. Does so by using
   :c:func:`reduce_pseudo_inverse` continually until the degree of
   the curve can no longer be reduced.

   :param int* num_nodes:
      **[Input]** The number of control points :math:`N` of a
      B |eacute| zier curve.
   :param int* dimension:
      **[Input]** The dimension :math:`D` such that the curve lies in
      :math:`\mathbf{R}^D`.
   :param double* nodes:
      **[Input]** The actual control points of the curve as a
      :math:`D \times N` array. This should be laid out in Fortran order,
      with :math:`D N` total values.
   :param int* num_reduced_nodes:
      **[Output]** The number of control points :math:`M` of the fully reduced
      curve.
   :param double* reduced:
      **[Output]** The control points of the fully reduced curve as a
      :math:`D \times N` array. The first :math:`M` columns will contain the
      reduced nodes. ``reduced`` must be allocated by the caller and since
      :math:`M = N` occurs when no reduction is possible, this array must be
      :math:`D \times N`.
   :param bool* not_implemented:
      **[Output]** Indicates if degree-reduction has been implemented for the
      current curve's degree. (Currently, the only degrees supported are 1,
      2, 3 and  4.)

   **Signature:**

   .. code-block:: c

      void
      full_reduce(int *num_nodes,
                  int *dimension,
                  double *nodes,
                  int *num_reduced_nodes,
                  double *reduced,
                  bool *not_implemented);

.. c:function:: void get_curvature(int *num_nodes, \
                                   int *dimension, \
                                   double *nodes, \
                                   double *tangent_vec, \
                                   double *s, \
                                   double *curvature)

   Get the curvature of a B |eacute| zier curve at a point. See
   :func:`._get_curvature` for more details.

   :param int* num_nodes:
      **[Input]** The number of control points :math:`N` of a
      B |eacute| zier curve.
   :param int* dimension:
      **[Input]** The dimension :math:`D` such that the curve lies in
      :math:`\mathbf{R}^D`.
   :param double* nodes:
      **[Input]** The actual control points of the curve as a
      :math:`D \times N` array. This should be laid out in Fortran order,
      with :math:`D N` total values.
   :param double* tangent_vec:
      **[Input]** The hodograph :math:`B'(s)` as a :math:`D \times 1` array.
      Note that this could be computed once :math:`s` and :math:`B` are known,
      but this allows the caller to re-use an already computed tangent vector.
   :param double* s:
      **[Input]** The parameter :math:`s` where the curvature is being
      computed.
   :param double* curvature:
      **[Output]** The curvature :math:`\kappa`.

   **Signature:**

   .. code-block:: c

      void
      get_curvature(int *num_nodes,
                    int *dimension,
                    double *nodes,
                    double *tangent_vec,
                    double *s,
                    double *curvature);

.. c:function:: void locate_point_curve(int *num_nodes, \
                                        int *dimension, \
                                        double *nodes, \
                                        double *point, \
                                        double *s_approx)

   This solves the inverse problem :math:`B(s) = p` (if it can be
   solved). Does so by subdividing the curve until the segments are
   sufficiently small, then using Newton's method to narrow in on the
   pre-image of the point.

   :param int* num_nodes:
      **[Input]** The number of control points :math:`N` of a
      B |eacute| zier curve.
   :param int* dimension:
      **[Input]** The dimension :math:`D` such that the curve lies in
      :math:`\mathbf{R}^D`.
   :param double* nodes:
      **[Input]** The actual control points of the curve as a
      :math:`D \times N` array. This should be laid out in Fortran order,
      with :math:`D N` total values.
   :param double* point:
      **[Input]** The point :math:`p` as a :math:`D \times 1` array.
   :param double* s_approx:
      **[Output]** The parameter :math:`s` of the solution. If
      :math:`p` can't be located on the surface, then ``s_approx = -1.0``.
      If there are **multiple** parameters that satisfy :math:`B(s) = p`
      (indicating that :math:`B(s)` has a self-crossing) then
      ``s_approx = -2.0``.

   **Signature:**

   .. code-block:: c

      void
      locate_point_curve(int *num_nodes,
                         int *dimension,
                         double *nodes,
                         double *point,
                         double *s_approx);

.. c:function:: void newton_refine_curve(int *num_nodes, \
                                         int *dimension, \
                                         double *nodes, \
                                         double *point, \
                                         double *s, \
                                         double *updated_s)

   This refines a solution to :math:`B(s) = p` using Newton's
   method. Given a current approximation :math:`s_n` for a solution,
   this produces the updated approximation via

   .. math::

      s_{n + 1} = s_n - \frac{B'(s_n)^T \left[B(s_n) - p\right]}{
          B'(s_n)^T B'(s_n)}.

   :param int* num_nodes:
      **[Input]** The number of control points :math:`N` of a
      B |eacute| zier curve.
   :param int* dimension:
      **[Input]** The dimension :math:`D` such that the curve lies in
      :math:`\mathbf{R}^D`.
   :param double* nodes:
      **[Input]** The actual control points of the curve as a
      :math:`D \times N` array. This should be laid out in Fortran order,
      with :math:`D N` total values.
   :param double* point:
      **[Input]** The point :math:`p` as a :math:`D \times 1` array.
   :param double* s:
      **[Input]** The parameter :math:`s_n` of the current approximation
      of a solution.
   :param double* updated_s:
      **[Output]** The parameter :math:`s_{n + 1}` of the updated
      approximation.

   **Signature:**

   .. code-block:: c

      void
      newton_refine_curve(int *num_nodes,
                          int *dimension,
                          double *nodes,
                          double *point,
                          double *s,
                          double *updated_s);

.. c:function:: void reduce_pseudo_inverse(int *num_nodes, \
                                           int *dimension, \
                                           double *nodes, \
                                           double *reduced, \
                                           bool *not_implemented)

   Perform a pseudo inverse to :c:func:`elevate_nodes_curve`. If an
   inverse can be found, i.e. if a curve can be degree-reduced, then
   this will produce the equivalent curve of lower degree. If no
   inverse can be found, then this will produce the "best" answer in
   the least squares sense.

   :param int* num_nodes:
      **[Input]** The number of control points :math:`N` of a
      B |eacute| zier curve.
   :param int* dimension:
      **[Input]** The dimension :math:`D` such that the curve lies in
      :math:`\mathbf{R}^D`.
   :param double* nodes:
      **[Input]** The actual control points of the curve as a
      :math:`D \times N` array. This should be laid out in Fortran order,
      with :math:`D N` total values.
   :param double* reduced:
      **[Output]** The control points of the degree-(pseudo)reduced curve
      :math:`D \times (N - 1)` array, laid out in Fortran order.
   :param bool* not_implemented:
      **[Output]** Indicates if degree-reduction has been implemented for the
      current curve's degree. (Currently, the only degrees supported are 1,
      2, 3 and  4.)

   **Signature:**

   .. code-block:: c

      void
      reduce_pseudo_inverse(int *num_nodes,
                            int *dimension,
                            double *nodes,
                            double *reduced,
                            bool *not_implemented);

.. c:function:: void specialize_curve(int *num_nodes, \
                                      int *dimension, \
                                      double *nodes, \
                                      double *start, \
                                      double *end, \
                                      double *new_nodes)

   Specialize a B |eacute| zier curve to an interval
   :math:`\left[a, b\right]`. This produces the control points
   for the curve given by :math:`B\left(a + (b - a) s\right)`.

   :param int* num_nodes:
      **[Input]** The number of control points :math:`N` of a
      B |eacute| zier curve.
   :param int* dimension:
      **[Input]** The dimension :math:`D` such that the curve lies in
      :math:`\mathbf{R}^D`.
   :param double* nodes:
      **[Input]** The actual control points of the curve as a
      :math:`D \times N` array. This should be laid out in Fortran order,
      with :math:`D N` total values.
   :param double* start:
      **[Input]** The start :math:`a` of the specialized interval.
   :param double* end:
      **[Input]** The end :math:`b` of the specialized interval.
   :param double* new_nodes:
      **[Output]** The control points of the specialized curve, as a
      :math:`D \times N` array, laid out in Fortran order.

   **Signature:**

   .. code-block:: c

      void
      specialize_curve(int *num_nodes,
                       int *dimension,
                       double *nodes,
                       double *start,
                       double *end,
                       double *new_nodes);

.. c:function:: void subdivide_nodes_curve(int *num_nodes, \
                                           int *dimension, \
                                           double *nodes, \
                                           double *left_nodes, \
                                           double *right_nodes)

   Split a B |eacute| zier curve into two halves
   :math:`B\left(\left[0, \frac{1}{2}\right]\right)` and
   :math:`B\left(\left[\frac{1}{2}, 1\right]\right)`.

   :param int* num_nodes:
      **[Input]** The number of control points :math:`N` of a
      B |eacute| zier curve.
   :param int* dimension:
      **[Input]** The dimension :math:`D` such that the curve lies in
      :math:`\mathbf{R}^D`.
   :param double* nodes:
      **[Input]** The actual control points of the curve as a
      :math:`D \times N` array. This should be laid out in Fortran order,
      with :math:`D N` total values.
   :param double* left_nodes:
      **[Output]** The control points of the left half curve
      :math:`B\left(\left[0, \frac{1}{2}\right]\right)` as a
      :math:`D \times N` array, laid out in Fortran order.
   :param double* right_nodes:
      **[Output]** The control points of the right half curve
      :math:`B\left(\left[\frac{1}{2}, 1\right]\right)` as a
      :math:`D \times N` array, laid out in Fortran order.

   **Signature:**

   .. code-block:: c

      void
      subdivide_nodes_curve(int *num_nodes,
                            int *dimension,
                            double *nodes,
                            double *left_nodes,
                            double *right_nodes);